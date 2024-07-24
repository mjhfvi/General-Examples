#!/bin/bash
# Bash Menu Script Example

PS3='Please Enter Your Choice: '
options=("Check Tags" "Download Application" "Write Version to File?" "Quit")
select opt in "${options[@]}"
do
  case $opt in
    "Check Tags")
      echo "Check Tags for ElasticSearch"
      curl https://api.github.com/repos/elastic/elasticsearch/releases/latest
      ;;
    "Download Application")
      echo "you chose choice 2"
      ;;
    "Write Version to File?")
      echo "you chose choice $REPLY which is $opt"
      ;;
    "Quit")
      break
      ;;
    *) echo "invalid option $REPLY";;
  esac
done