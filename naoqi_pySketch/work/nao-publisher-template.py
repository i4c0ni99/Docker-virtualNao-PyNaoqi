#!PySketch/sketch-executor.py
import nao_execute_command
####################################################

# MUST be PySketch_py2
# linked as ./PySketch: ln -s ./PySketch_py2 ./PySketch

from PySketch.elapsedtime import ElapsedTime
from PySketch.abstractflow import FlowChannel
from PySketch.flowsync import FlowSync
from PySketch.flowproto import FlowChanID, Variant_T, Flow_T
from PySketch.robotmod import RobotModule

module = None
leftSonarChan = None

import time
import argparse

args = None

parser = argparse.ArgumentParser(description="Nao publisher")
parser.add_argument('sketchfile', help='Sketch program file')
parser.add_argument('--user', help='Flow-network username', default='guest')
parser.add_argument('--password', help='Flow-network password', default='password')

# IT REQUIREs TO IMPORT pynaqi library
from naoqi import ALProxy

memoryProxy = None
sonarProxy  = None

####################################################
# SKETCH

def setup():
    global args
    global parser
    global module
    global memoryProxy
    global sonarProxy
    
    args = parser.parse_args()

    module = RobotModule()
    module._userName = args.user
    module._passwd = args.password

    module.setNewChanCallBack(onChannelAdded)
    module.setDelChanCallBack(onChannelRemoved)

    # ONLY TO NOTIFY requestToStart AND requestToStop FOR PUBLISHING ACTIVITY
    module.setStartChanPubReqCallBack(onStartChanPub)
    module.setStopChanPubReqCallBack(onStopChanPub)

    # init Nao SETUP
    memoryProxy = ALProxy("ALMemory", "ip_macchina_host", 9559)
    sonarProxy = ALProxy("ALSonar", "ip_macchina_host", 9559)
    sonarProxy.subscribe("myApplication")
    # end Nao SETUP

    ok = module.connect()

    if ok:
        # Requests to SkRobot to ADD streaming channel with name: <username>.LeftSonar
        module.addStreamingChannel(Flow_T.FT_BLOB, Variant_T.T_FLOAT, "LeftSonar", "")

    # EXIT if connection is not VALID
    return ok

def loop():
    global module
    global memoryProxy
    global sonarProxy
    global leftSonarChan
    nao_execute_command.action()
    if leftSonarChan and leftSonarChan.isPublishingEnabled:
        # GRAB data FROM Nao
        leftSensor = memoryProxy.getData("Device/SubDeviceList/US/Left/Sensor/Value")

        # SEND data TO SkRobot
        module.publishFloat(leftSonarChan.chanID, leftSensor)

    
    # MUST TICK
    module.tick()

    # EXIT if connection is not VALID
    return module.isConnected()

####################################################
# CALLBACKs

def onChannelAdded(ch):
    global module
    global leftSonarChan

    if ch.name == "{}.LeftSonar".format(module._userName):
        leftSonarChan = ch
        # Requested Channel is ADDED on SkRobot
        print("LeftSonar Channel ready")

def onChannelRemoved(ch):
    global module
    global leftSonarChan

    if leftSonarChan and ch.name == leftSonarChan.name:
        leftSonarChan = None

def onStartChanPub(ch):
    global module
    global leftSonarChan

    if leftSonarChan and ch.name == leftSonarChan.name:
        print("SkRobot requested to START publishing on LeftSonar")

def onStopChanPub(ch):
    global module
    global leftSonarChan

    if leftSonarChan and ch.name == leftSonarChan.name:
        print("SkRobot requested to STOP publishing on LeftSonar")

####################################################
