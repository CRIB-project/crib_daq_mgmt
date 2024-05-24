#!/bin/sh

#DATADIR=/data2/$EXP_NAME
#BASEDIR=$(dirname "$0")

rsync -auv "/Data/$EXP_NAME" "cribana:/Data"
