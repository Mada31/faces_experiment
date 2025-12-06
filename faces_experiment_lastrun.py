#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on December 06, 2025, at 18:52
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'faces_experiment'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [2560, 1440]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\cimpe\\OneDrive - Aarhus universitet\\Desktop\\Faces Experiment\\faces_experiment_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "introduction" ---
    introduction_text = visual.TextStim(win=win, name='introduction_text',
        text='Welcome!\n\nIn this experiment, you will see a series of faces showing different emotional expressions.\n\nYour task is to identify which emotion is being expressed by selecting one of the buttons below each face.\n\nPlease try to respond as accurately and as quickly as possible.\n\nWhen you are ready to begin, press the Start button below.',
        font='Arial',
        pos=(0, 0.1), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    btn_start = visual.ButtonStim(win, 
        text='Start', font='Arvo',
        pos=(0, -0.3),
        letterHeight=0.04,
        size=(0.35, 0.15), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='black', borderColor='black',
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='btn_start',
        depth=-1
    )
    btn_start.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "trial_face" ---
    image_stim = visual.ImageStim(
        win=win,
        name='image_stim', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "trial_response" ---
    btn_anger_2 = visual.ButtonStim(win, 
        text='Anger', font='Arvo',
        pos=(-0.40, -0.25),
        letterHeight=0.04,
        size=(0.30, 0.12), 
        ori=0.0
        ,borderWidth=2.0,
        fillColor='black', borderColor='black',
        color='white', colorSpace='rgb',
        opacity=1.0,
        bold=True, italic=False,
        padding=0.02,
        anchor='center',
        name='btn_anger_2',
        depth=0
    )
    btn_anger_2.buttonClock = core.Clock()
    btn_disgust_2 = visual.ButtonStim(win, 
        text='Disgust', font='Arvo',
        pos=(0.00, -0.25),
        letterHeight=0.04,
        size=(0.30, 0.12), 
        ori=0.0
        ,borderWidth=2.0,
        fillColor='black', borderColor='black',
        color='white', colorSpace='rgb',
        opacity=1.0,
        bold=True, italic=False,
        padding=0.02,
        anchor='center',
        name='btn_disgust_2',
        depth=-1
    )
    btn_disgust_2.buttonClock = core.Clock()
    btn_fear_2 = visual.ButtonStim(win, 
        text='Fear', font='Arvo',
        pos=(0.40, -0.25),
        letterHeight=0.04,
        size=(0.30, 0.12), 
        ori=0.0
        ,borderWidth=2.0,
        fillColor='black', borderColor='black',
        color='white', colorSpace='rgb',
        opacity=1.0,
        bold=True, italic=False,
        padding=0.02,
        anchor='center',
        name='btn_fear_2',
        depth=-2
    )
    btn_fear_2.buttonClock = core.Clock()
    btn_happiness_2 = visual.ButtonStim(win, 
        text='Happiness', font='Arvo',
        pos=(-0.40, -0.40),
        letterHeight=0.04,
        size=(0.30, 0.12), 
        ori=0.0
        ,borderWidth=2.0,
        fillColor='black', borderColor='black',
        color='white', colorSpace='rgb',
        opacity=1.0,
        bold=True, italic=False,
        padding=0.02,
        anchor='center',
        name='btn_happiness_2',
        depth=-3
    )
    btn_happiness_2.buttonClock = core.Clock()
    btn_neutrality_2 = visual.ButtonStim(win, 
        text='Neutrality', font='Arvo',
        pos=(0.00, -0.40),
        letterHeight=0.04,
        size=(0.30, 0.12), 
        ori=0.0
        ,borderWidth=2.0,
        fillColor='black', borderColor='black',
        color='white', colorSpace='rgb',
        opacity=1.0,
        bold=True, italic=False,
        padding=0.02,
        anchor='center',
        name='btn_neutrality_2',
        depth=-4
    )
    btn_neutrality_2.buttonClock = core.Clock()
    btn_sadness_2 = visual.ButtonStim(win, 
        text='Sadness', font='Arvo',
        pos=(0.40, -0.40),
        letterHeight=0.04,
        size=(0.30, 0.12), 
        ori=0.0
        ,borderWidth=2.0,
        fillColor='black', borderColor='black',
        color='white', colorSpace='rgb',
        opacity=1.0,
        bold=True, italic=False,
        padding=0.02,
        anchor='center',
        name='btn_sadness_2',
        depth=-5
    )
    btn_sadness_2.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "end_screen" ---
    text = visual.TextStim(win=win, name='text',
        text='Thank you for participating. \nYou may now close the browser window.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "introduction" ---
    # create an object to store info about Routine introduction
    introduction = data.Routine(
        name='introduction',
        components=[introduction_text, btn_start],
    )
    introduction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # reset btn_start to account for continued clicks & clear times on/off
    btn_start.reset()
    # store start times for introduction
    introduction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    introduction.tStart = globalClock.getTime(format='float')
    introduction.status = STARTED
    thisExp.addData('introduction.started', introduction.tStart)
    introduction.maxDuration = None
    # keep track of which components have finished
    introductionComponents = introduction.components
    for thisComponent in introduction.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "introduction" ---
    introduction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *introduction_text* updates
        
        # if introduction_text is starting this frame...
        if introduction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            introduction_text.frameNStart = frameN  # exact frame index
            introduction_text.tStart = t  # local t and not account for scr refresh
            introduction_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(introduction_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'introduction_text.started')
            # update status
            introduction_text.status = STARTED
            introduction_text.setAutoDraw(True)
        
        # if introduction_text is active this frame...
        if introduction_text.status == STARTED:
            # update params
            pass
        # *btn_start* updates
        
        # if btn_start is starting this frame...
        if btn_start.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            btn_start.frameNStart = frameN  # exact frame index
            btn_start.tStart = t  # local t and not account for scr refresh
            btn_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(btn_start, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'btn_start.started')
            # update status
            btn_start.status = STARTED
            win.callOnFlip(btn_start.buttonClock.reset)
            btn_start.setAutoDraw(True)
        
        # if btn_start is active this frame...
        if btn_start.status == STARTED:
            # update params
            pass
            # check whether btn_start has been pressed
            if btn_start.isClicked:
                if not btn_start.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    btn_start.timesOn.append(btn_start.buttonClock.getTime())
                    btn_start.timesOff.append(btn_start.buttonClock.getTime())
                elif len(btn_start.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    btn_start.timesOff[-1] = btn_start.buttonClock.getTime()
                if not btn_start.wasClicked:
                    # end routine when btn_start is clicked
                    continueRoutine = False
                if not btn_start.wasClicked:
                    # run callback code when btn_start is clicked
                    pass
        # take note of whether btn_start was clicked, so that next frame we know if clicks are new
        btn_start.wasClicked = btn_start.isClicked and btn_start.status == STARTED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=introduction,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            introduction.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in introduction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "introduction" ---
    for thisComponent in introduction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for introduction
    introduction.tStop = globalClock.getTime(format='float')
    introduction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('introduction.stopped', introduction.tStop)
    thisExp.addData('btn_start.numClicks', btn_start.numClicks)
    if btn_start.numClicks:
       thisExp.addData('btn_start.timesOn', btn_start.timesOn)
       thisExp.addData('btn_start.timesOff', btn_start.timesOff)
    else:
       thisExp.addData('btn_start.timesOn', "")
       thisExp.addData('btn_start.timesOff', "")
    thisExp.nextEntry()
    # the Routine "introduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('conditions_faces.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        trials.status = STARTED
        if hasattr(thisTrial, 'status'):
            thisTrial.status = STARTED
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "trial_face" ---
        # create an object to store info about Routine trial_face
        trial_face = data.Routine(
            name='trial_face',
            components=[image_stim],
        )
        trial_face.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        image_stim.setImage(image_file)
        # store start times for trial_face
        trial_face.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial_face.tStart = globalClock.getTime(format='float')
        trial_face.status = STARTED
        thisExp.addData('trial_face.started', trial_face.tStart)
        trial_face.maxDuration = None
        # keep track of which components have finished
        trial_faceComponents = trial_face.components
        for thisComponent in trial_face.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial_face" ---
        trial_face.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_stim* updates
            
            # if image_stim is starting this frame...
            if image_stim.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_stim.frameNStart = frameN  # exact frame index
                image_stim.tStart = t  # local t and not account for scr refresh
                image_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_stim.started')
                # update status
                image_stim.status = STARTED
                image_stim.setAutoDraw(True)
            
            # if image_stim is active this frame...
            if image_stim.status == STARTED:
                # update params
                pass
            
            # if image_stim is stopping this frame...
            if image_stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_stim.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    image_stim.tStop = t  # not accounting for scr refresh
                    image_stim.tStopRefresh = tThisFlipGlobal  # on global time
                    image_stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_stim.stopped')
                    # update status
                    image_stim.status = FINISHED
                    image_stim.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trial_face,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trial_face.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_face.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_face" ---
        for thisComponent in trial_face.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial_face
        trial_face.tStop = globalClock.getTime(format='float')
        trial_face.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial_face.stopped', trial_face.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if trial_face.maxDurationReached:
            routineTimer.addTime(-trial_face.maxDuration)
        elif trial_face.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        
        # --- Prepare to start Routine "trial_response" ---
        # create an object to store info about Routine trial_response
        trial_response = data.Routine(
            name='trial_response',
            components=[btn_anger_2, btn_disgust_2, btn_fear_2, btn_happiness_2, btn_neutrality_2, btn_sadness_2],
        )
        trial_response.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # reset btn_anger_2 to account for continued clicks & clear times on/off
        btn_anger_2.reset()
        # reset btn_disgust_2 to account for continued clicks & clear times on/off
        btn_disgust_2.reset()
        # reset btn_fear_2 to account for continued clicks & clear times on/off
        btn_fear_2.reset()
        # reset btn_happiness_2 to account for continued clicks & clear times on/off
        btn_happiness_2.reset()
        # reset btn_neutrality_2 to account for continued clicks & clear times on/off
        btn_neutrality_2.reset()
        # reset btn_sadness_2 to account for continued clicks & clear times on/off
        btn_sadness_2.reset()
        # Run 'Begin Routine' code from code_correctness_2
        clickedEmotion = ""
        
        # store start times for trial_response
        trial_response.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial_response.tStart = globalClock.getTime(format='float')
        trial_response.status = STARTED
        thisExp.addData('trial_response.started', trial_response.tStart)
        trial_response.maxDuration = None
        # keep track of which components have finished
        trial_responseComponents = trial_response.components
        for thisComponent in trial_response.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial_response" ---
        trial_response.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *btn_anger_2* updates
            
            # if btn_anger_2 is starting this frame...
            if btn_anger_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                btn_anger_2.frameNStart = frameN  # exact frame index
                btn_anger_2.tStart = t  # local t and not account for scr refresh
                btn_anger_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(btn_anger_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'btn_anger_2.started')
                # update status
                btn_anger_2.status = STARTED
                win.callOnFlip(btn_anger_2.buttonClock.reset)
                btn_anger_2.setAutoDraw(True)
            
            # if btn_anger_2 is active this frame...
            if btn_anger_2.status == STARTED:
                # update params
                pass
                # check whether btn_anger_2 has been pressed
                if btn_anger_2.isClicked:
                    if not btn_anger_2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        btn_anger_2.timesOn.append(btn_anger_2.buttonClock.getTime())
                        btn_anger_2.timesOff.append(btn_anger_2.buttonClock.getTime())
                    elif len(btn_anger_2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        btn_anger_2.timesOff[-1] = btn_anger_2.buttonClock.getTime()
                    if not btn_anger_2.wasClicked:
                        # end routine when btn_anger_2 is clicked
                        continueRoutine = False
                    if not btn_anger_2.wasClicked:
                        # run callback code when btn_anger_2 is clicked
                        clickedEmotion = "anger"
            # take note of whether btn_anger_2 was clicked, so that next frame we know if clicks are new
            btn_anger_2.wasClicked = btn_anger_2.isClicked and btn_anger_2.status == STARTED
            # *btn_disgust_2* updates
            
            # if btn_disgust_2 is starting this frame...
            if btn_disgust_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                btn_disgust_2.frameNStart = frameN  # exact frame index
                btn_disgust_2.tStart = t  # local t and not account for scr refresh
                btn_disgust_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(btn_disgust_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'btn_disgust_2.started')
                # update status
                btn_disgust_2.status = STARTED
                win.callOnFlip(btn_disgust_2.buttonClock.reset)
                btn_disgust_2.setAutoDraw(True)
            
            # if btn_disgust_2 is active this frame...
            if btn_disgust_2.status == STARTED:
                # update params
                pass
                # check whether btn_disgust_2 has been pressed
                if btn_disgust_2.isClicked:
                    if not btn_disgust_2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        btn_disgust_2.timesOn.append(btn_disgust_2.buttonClock.getTime())
                        btn_disgust_2.timesOff.append(btn_disgust_2.buttonClock.getTime())
                    elif len(btn_disgust_2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        btn_disgust_2.timesOff[-1] = btn_disgust_2.buttonClock.getTime()
                    if not btn_disgust_2.wasClicked:
                        # end routine when btn_disgust_2 is clicked
                        continueRoutine = False
                    if not btn_disgust_2.wasClicked:
                        # run callback code when btn_disgust_2 is clicked
                        clickedEmotion = "disgust"
            # take note of whether btn_disgust_2 was clicked, so that next frame we know if clicks are new
            btn_disgust_2.wasClicked = btn_disgust_2.isClicked and btn_disgust_2.status == STARTED
            # *btn_fear_2* updates
            
            # if btn_fear_2 is starting this frame...
            if btn_fear_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                btn_fear_2.frameNStart = frameN  # exact frame index
                btn_fear_2.tStart = t  # local t and not account for scr refresh
                btn_fear_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(btn_fear_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'btn_fear_2.started')
                # update status
                btn_fear_2.status = STARTED
                win.callOnFlip(btn_fear_2.buttonClock.reset)
                btn_fear_2.setAutoDraw(True)
            
            # if btn_fear_2 is active this frame...
            if btn_fear_2.status == STARTED:
                # update params
                pass
                # check whether btn_fear_2 has been pressed
                if btn_fear_2.isClicked:
                    if not btn_fear_2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        btn_fear_2.timesOn.append(btn_fear_2.buttonClock.getTime())
                        btn_fear_2.timesOff.append(btn_fear_2.buttonClock.getTime())
                    elif len(btn_fear_2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        btn_fear_2.timesOff[-1] = btn_fear_2.buttonClock.getTime()
                    if not btn_fear_2.wasClicked:
                        # end routine when btn_fear_2 is clicked
                        continueRoutine = False
                    if not btn_fear_2.wasClicked:
                        # run callback code when btn_fear_2 is clicked
                        clickedEmotion = "fear"
            # take note of whether btn_fear_2 was clicked, so that next frame we know if clicks are new
            btn_fear_2.wasClicked = btn_fear_2.isClicked and btn_fear_2.status == STARTED
            # *btn_happiness_2* updates
            
            # if btn_happiness_2 is starting this frame...
            if btn_happiness_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                btn_happiness_2.frameNStart = frameN  # exact frame index
                btn_happiness_2.tStart = t  # local t and not account for scr refresh
                btn_happiness_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(btn_happiness_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'btn_happiness_2.started')
                # update status
                btn_happiness_2.status = STARTED
                win.callOnFlip(btn_happiness_2.buttonClock.reset)
                btn_happiness_2.setAutoDraw(True)
            
            # if btn_happiness_2 is active this frame...
            if btn_happiness_2.status == STARTED:
                # update params
                pass
                # check whether btn_happiness_2 has been pressed
                if btn_happiness_2.isClicked:
                    if not btn_happiness_2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        btn_happiness_2.timesOn.append(btn_happiness_2.buttonClock.getTime())
                        btn_happiness_2.timesOff.append(btn_happiness_2.buttonClock.getTime())
                    elif len(btn_happiness_2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        btn_happiness_2.timesOff[-1] = btn_happiness_2.buttonClock.getTime()
                    if not btn_happiness_2.wasClicked:
                        # end routine when btn_happiness_2 is clicked
                        continueRoutine = False
                    if not btn_happiness_2.wasClicked:
                        # run callback code when btn_happiness_2 is clicked
                        clickedEmotion = "happiness"
            # take note of whether btn_happiness_2 was clicked, so that next frame we know if clicks are new
            btn_happiness_2.wasClicked = btn_happiness_2.isClicked and btn_happiness_2.status == STARTED
            # *btn_neutrality_2* updates
            
            # if btn_neutrality_2 is starting this frame...
            if btn_neutrality_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                btn_neutrality_2.frameNStart = frameN  # exact frame index
                btn_neutrality_2.tStart = t  # local t and not account for scr refresh
                btn_neutrality_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(btn_neutrality_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'btn_neutrality_2.started')
                # update status
                btn_neutrality_2.status = STARTED
                win.callOnFlip(btn_neutrality_2.buttonClock.reset)
                btn_neutrality_2.setAutoDraw(True)
            
            # if btn_neutrality_2 is active this frame...
            if btn_neutrality_2.status == STARTED:
                # update params
                pass
                # check whether btn_neutrality_2 has been pressed
                if btn_neutrality_2.isClicked:
                    if not btn_neutrality_2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        btn_neutrality_2.timesOn.append(btn_neutrality_2.buttonClock.getTime())
                        btn_neutrality_2.timesOff.append(btn_neutrality_2.buttonClock.getTime())
                    elif len(btn_neutrality_2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        btn_neutrality_2.timesOff[-1] = btn_neutrality_2.buttonClock.getTime()
                    if not btn_neutrality_2.wasClicked:
                        # end routine when btn_neutrality_2 is clicked
                        continueRoutine = False
                    if not btn_neutrality_2.wasClicked:
                        # run callback code when btn_neutrality_2 is clicked
                        clickedEmotion = "neutrality"
            # take note of whether btn_neutrality_2 was clicked, so that next frame we know if clicks are new
            btn_neutrality_2.wasClicked = btn_neutrality_2.isClicked and btn_neutrality_2.status == STARTED
            # *btn_sadness_2* updates
            
            # if btn_sadness_2 is starting this frame...
            if btn_sadness_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                btn_sadness_2.frameNStart = frameN  # exact frame index
                btn_sadness_2.tStart = t  # local t and not account for scr refresh
                btn_sadness_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(btn_sadness_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'btn_sadness_2.started')
                # update status
                btn_sadness_2.status = STARTED
                win.callOnFlip(btn_sadness_2.buttonClock.reset)
                btn_sadness_2.setAutoDraw(True)
            
            # if btn_sadness_2 is active this frame...
            if btn_sadness_2.status == STARTED:
                # update params
                pass
                # check whether btn_sadness_2 has been pressed
                if btn_sadness_2.isClicked:
                    if not btn_sadness_2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        btn_sadness_2.timesOn.append(btn_sadness_2.buttonClock.getTime())
                        btn_sadness_2.timesOff.append(btn_sadness_2.buttonClock.getTime())
                    elif len(btn_sadness_2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        btn_sadness_2.timesOff[-1] = btn_sadness_2.buttonClock.getTime()
                    if not btn_sadness_2.wasClicked:
                        # end routine when btn_sadness_2 is clicked
                        continueRoutine = False
                    if not btn_sadness_2.wasClicked:
                        # run callback code when btn_sadness_2 is clicked
                        clickedEmotion = "sadness"
            # take note of whether btn_sadness_2 was clicked, so that next frame we know if clicks are new
            btn_sadness_2.wasClicked = btn_sadness_2.isClicked and btn_sadness_2.status == STARTED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trial_response,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trial_response.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_response.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_response" ---
        for thisComponent in trial_response.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial_response
        trial_response.tStop = globalClock.getTime(format='float')
        trial_response.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial_response.stopped', trial_response.tStop)
        trials.addData('btn_anger_2.numClicks', btn_anger_2.numClicks)
        if btn_anger_2.numClicks:
           trials.addData('btn_anger_2.timesOn', btn_anger_2.timesOn)
           trials.addData('btn_anger_2.timesOff', btn_anger_2.timesOff)
        else:
           trials.addData('btn_anger_2.timesOn', "")
           trials.addData('btn_anger_2.timesOff', "")
        trials.addData('btn_disgust_2.numClicks', btn_disgust_2.numClicks)
        if btn_disgust_2.numClicks:
           trials.addData('btn_disgust_2.timesOn', btn_disgust_2.timesOn)
           trials.addData('btn_disgust_2.timesOff', btn_disgust_2.timesOff)
        else:
           trials.addData('btn_disgust_2.timesOn', "")
           trials.addData('btn_disgust_2.timesOff', "")
        trials.addData('btn_fear_2.numClicks', btn_fear_2.numClicks)
        if btn_fear_2.numClicks:
           trials.addData('btn_fear_2.timesOn', btn_fear_2.timesOn)
           trials.addData('btn_fear_2.timesOff', btn_fear_2.timesOff)
        else:
           trials.addData('btn_fear_2.timesOn', "")
           trials.addData('btn_fear_2.timesOff', "")
        trials.addData('btn_happiness_2.numClicks', btn_happiness_2.numClicks)
        if btn_happiness_2.numClicks:
           trials.addData('btn_happiness_2.timesOn', btn_happiness_2.timesOn)
           trials.addData('btn_happiness_2.timesOff', btn_happiness_2.timesOff)
        else:
           trials.addData('btn_happiness_2.timesOn', "")
           trials.addData('btn_happiness_2.timesOff', "")
        trials.addData('btn_neutrality_2.numClicks', btn_neutrality_2.numClicks)
        if btn_neutrality_2.numClicks:
           trials.addData('btn_neutrality_2.timesOn', btn_neutrality_2.timesOn)
           trials.addData('btn_neutrality_2.timesOff', btn_neutrality_2.timesOff)
        else:
           trials.addData('btn_neutrality_2.timesOn', "")
           trials.addData('btn_neutrality_2.timesOff', "")
        trials.addData('btn_sadness_2.numClicks', btn_sadness_2.numClicks)
        if btn_sadness_2.numClicks:
           trials.addData('btn_sadness_2.timesOn', btn_sadness_2.timesOn)
           trials.addData('btn_sadness_2.timesOff', btn_sadness_2.timesOff)
        else:
           trials.addData('btn_sadness_2.timesOn', "")
           trials.addData('btn_sadness_2.timesOff', "")
        # Run 'End Routine' code from code_correctness_2
        # Save the emotion clicked (set by the button's callback)
        thisExp.addData("clickedEmotion", clickedEmotion)
        
        # Compute correctness
        correct = int(clickedEmotion == correct_emotion)
        
        # Save correctness
        thisExp.addData("correct", correct)
        
        
        # the Routine "trial_response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTrial as finished
        if hasattr(thisTrial, 'status'):
            thisTrial.status = FINISHED
        # if awaiting a pause, pause now
        if trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "end_screen" ---
    # create an object to store info about Routine end_screen
    end_screen = data.Routine(
        name='end_screen',
        components=[text],
    )
    end_screen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for end_screen
    end_screen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end_screen.tStart = globalClock.getTime(format='float')
    end_screen.status = STARTED
    thisExp.addData('end_screen.started', end_screen.tStart)
    end_screen.maxDuration = None
    # keep track of which components have finished
    end_screenComponents = end_screen.components
    for thisComponent in end_screen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end_screen" ---
    end_screen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=end_screen,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            end_screen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_screen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_screen" ---
    for thisComponent in end_screen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end_screen
    end_screen.tStop = globalClock.getTime(format='float')
    end_screen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end_screen.stopped', end_screen.tStop)
    thisExp.nextEntry()
    # the Routine "end_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
