#!usr/bin/env bash 

# Wait time
WAIT="24 hours"
process_started=false
tmp_pid=0

# For starting a detached process
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
        # Process has been exited normally.
        # Resetting the trigger.
        TRIGGER=$(date +'%d-%m-%y-%H-%M' -d "$WAIT")
        echo "New run in $WAIT: $TRIGGER"
      else
        echo "Script exited with an error"
        # Here. e. g. Start the script again
        startProcess
        echo "Retarted script: "  $(date +'%d-%m-%y %H:%M:%S') " (PID $tmp_pid)"
      fi

    fi
    sleep 1s
  fi
  
done