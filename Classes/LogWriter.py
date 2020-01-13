from datetime import datetime

now = datetime.now()


def write_log(time, run_time, action):
    f = open("LOG.txt", "a")
    f.write(str(time) + " RUN-TIME: " + str(run_time) + " LOG: " + str(action) + "\n")
    f.close()
