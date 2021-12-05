#!usr/bin/env bash 

# Wait time
WAIT="24 hours"
process_started=false
tmp_pid=0

startProcess() { 
    ./formfill.py &>/dev/null &
    tmp_pid=$(echo $!)
    process_started=true;
    return 0
}

while true
do
    if [ "$process_started" = false ]; then
      startProcess
      echo "Started script: "  $(date +'%d-%m-%y %H:%M:%S') " (PID $tmp_pid)"
    fi

    if ! kill -0 $tmp_pid > /dev/null 2>&1; then
      echo "No process found with pid $tmp_pid" >&2
      wait ${tmp_pid}
      if [ $? -eq 0 ]; then
       echo "Script exited normal: " $(date +'%d-%m-%y %H:%M:%S')" . Waiting another $WAIT"
      else
        echo "Script exited with an error"
        startProcess
        echo "Retarted script: "  $(date +'%d-%m-%y %H:%M:%S') " (PID $tmp_pid)"
      fi

    fi
    sleep 1s
  fi
  
done
