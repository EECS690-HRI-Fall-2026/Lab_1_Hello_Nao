import sys, time, os, qi

if len(sys.argv) > 1 and len(sys.argv) < 3:
    ROBOT_IP = sys.argv[1]
    ROBOT_PORT = 9559
else:
    print("please provide proper number of arguments")
    print("Proper program usage: python3 nao_introduction.py IP_ADDRESS_HERE")
    sys.exit(1)

def main():
    session = qi.Session()
    try:
        print(f"Connecting to NAO at {ROBOT_IP}:{ROBOT_PORT}...")
        session.connect(f"tcp://{ROBOT_IP}:{ROBOT_PORT}")
        print("Successfully connected to NAO!")
    except RuntimeError as e:
        print(f"Failed to connect to the robot at {ROBOT_IP}: {e}")
        print("Please try again")
        sys.exit(1)

    try:
        tts = session.service("ALTextToSpeech")
    except Exception as e:
        print(f"Failed to load services: {e}")
        sys.exit(1)

    tts.say("Hello! My name is Nao!")
    
    #TODO finish Nao's introduction

if __name__ == "__main__":
    main()
