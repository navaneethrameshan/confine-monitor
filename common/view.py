from bottle import route, run, template
import json, string
from client.main import config, log


@route('/')
def index():
    return template('<b>Monitoring client</b>!')


@route('/get/all/seqnumber=<seqnumber:int>')
def getallinfo(seqnumber=0):

    json_value = {}

    config.update_last_seen_seq_number(seqnumber)
    # TODO: remove log entry for all entries until the last seen sequence number


    json_value = json.dumps(log.get_all_info_since(seqnumber), sort_keys=True, indent=4, separators=(',', ': '))


    if json_value:
        return json_value

def main(host='147.83.35.241', port=8080):
    run(host=host,port=port)

if __name__ == '__main__':
    main()
