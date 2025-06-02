from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask import session
from ebay.Entities.search_matches import *

from buysight.app_logic import AppLogic
import secrets
app = Flask(__name__)
CORS(app, supports_credentials=True, origins="*")
app.secret_key = secrets.token_hex(16)

app_logic = AppLogic()


@app.route("/")
def home():
    return render_template("index.html")


def make_titles_list(user_msg: str) -> List[str]:
    """
    :param user_msg: user_mag is a list of products requested to search by
    the user
    :return: list of strings - product titles to search
    """
    titles: List[str] = user_msg.split('\n')
    return titles


def print_search_results(search_matches: SearchMatches):
    """This function receive a search matches instance and creates a json object
    for the UI to print in chat box"""
    output = {}
    for title, items in search_matches.get_matches().items():
        output[title] = [item.to_dict() for item in items]
        if not output[title]:
            output[title] = [{title: "No results"}]
            print(output[title])
    return jsonify(output)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message: str = data.get("message", "").strip()

    print(dict(session))
    user_messages = session.get('messages', [])
    user_messages.append(user_message)
    session['messages'] = user_messages
    print(dict(session))

    # if user_message.lower() == "finish":
    #     print(user_messages[len(user_messages) - 2])
    #     search_matches = app_logic.search_items(user_messages[len(user_messages) - 2])
    #     return print_search_results(search_matches)

    print(user_message)
    search_matches = app_logic.search_items(user_message)
    return print_search_results(search_matches)

    #return jsonify({"response": f"BuySight Bot: received \"{user_message}\"!"})


if __name__ == "__main__":
    app.run(debug=True)
