#!/bin/sh

DATADIR=/data2/$EXP_NAME
BASEDIR=$(dirname $0)

rsync -auv /data2/$EXP_NAME/ cribana:/Data/$EXP_NAME

