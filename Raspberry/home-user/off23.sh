#!/bin/bash

# Do some basic checks

if [ "13" = "" ]
then
  echo "Usage: 0 gpio"
  exit 1
fi

# Check if gpio is already exported

if [ ! -d /sys/class/gpio/gpio13 ]
then
  echo 13 > /sys/class/gpio/export
  sleep 1 ;
fi

# Set to output
echo "out" > /sys/class/gpio/gpio13/direction

# Set to high value
echo 0 > /sys/class/gpio/gpio13/value
