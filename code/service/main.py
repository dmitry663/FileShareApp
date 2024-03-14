import env
import arg
import app

def main():
    app.run(host=env.host, port=arg.server_port, debug=env.debug)

if __name__ == '__main__':
    main()
    