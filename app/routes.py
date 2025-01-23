import os
import openai
import json
from sqlalchemy import text
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, current_app, session
from app import db

main_blueprint = Blueprint('index', __name__)

@main_blueprint.route('/', methods=['GET', 'POST'])
@main_blueprint.route('/home', methods=['GET', 'POST'])
def home():
    # Retrieve data from session
    table = session.pop('table', None)
    headers = session.pop('headers', None)
    summary = session.pop('summary', None)
    update_message = session.pop('update_message', "No data to display. Submit a query to generate results.")

    return render_template('index.html', table=table, summary=summary, headers=headers, update_message=update_message)


@main_blueprint.route('/submit_query', methods=['POST'])
def submit_query():
    # the system_message provides the model with much context about the database schema
    # and expectations in terms of its response generation
    system_message = """ 
            You are an expert in SQL operations and relational database. The database you're working with
            has the following schema:

            - Student(student_id, first_name, last_name, initial, username, email, password_hash, mentor)
            - Alum(alum_id, first_name, last_name, initial, username, email, password_hash)
            -Posts(post_id, title, content, timestamp, image_data, image_content_type, video_data, video_content_type,
                    event_name, event_date, event_description, user_id, author)
            
            In your reponse, include column name headers. Always provide your response in the JSON format below:
            {"summary": "generated summary", "query": "generated SQL query"}

            In this JSON response format, substitute "generated summary" with a conscise summary of the what the table generated
            using the query contains. if the query results in changes to any record in any table, add their first name and last name 
            to the summary

            In this JSON response format, substitute "generated SQL query" with SQL query to retrieve the requested data by 
            the user. 
            Remember, respond with only JSON in the format specified above
         """

    # stores the frontend message(in Natural Language) from the user
    user_query = request.form.get('query')

    if not user_query or user_query.strip() == "":
        return jsonify({"error": "No query provided. Please provide a valid natural language query."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_query}
            ],
            max_tokens=1500,
            temperature=0
        )

        ai_response = response['choices'][0]['message']['content'].strip()
        ai_response = json.loads(ai_response)

        if not ai_response:
            return jsonify({"error": "The AI could not generate a valid SQLAlchemy command."})
        query = ai_response["query"]
        print('This is the generatd query\n',query)
        summary = ai_response["summary"]
        print('\nThis is a description of the table\n',summary)

        update_message = "No data to display. Submit a query to generate results."

        try:
            results = db.session.execute(text(query))

            if query.startswith("SELECT"):
                rows = results.fetchall() # returns a list of Row objects
                headers = list(results.keys())
                session['table'] = [list(row) for row in rows]  
                session['headers'] = headers
            else:
                update_message = 'Query successfully executed'
                db.session.commit()


            session['summary'] = summary
            session['update_message'] = update_message

            return redirect(url_for('index.home'))
        except Exception as db_error:
            db.session.rollback()
            return jsonify({"error": str(db_error), "command": ai_response})
    except Exception as api_error:
        return jsonify({"error": "Failed to generate SQLAlchemy command.", "details": str(api_error)})