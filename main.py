from website import create_app

app = create_app() 

# run the server
if __name__ == '__main__': 
    # restart every time we make a change with the code
    app.run(debug=True)