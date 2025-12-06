/************************* 
 * Faces_Experiment *
 *************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2025.1.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'faces_experiment';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(introductionRoutineBegin());
flowScheduler.add(introductionRoutineEachFrame());
flowScheduler.add(introductionRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);



flowScheduler.add(end_screenRoutineBegin());
flowScheduler.add(end_screenRoutineEachFrame());
flowScheduler.add(end_screenRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'conditions_faces.xlsx', 'path': 'conditions_faces.xlsx'},
    {'name': 'faces/004_o_m_a_a.jpg', 'path': 'faces/004_o_m_a_a.jpg'},
    {'name': 'faces/004_o_m_a_b.jpg', 'path': 'faces/004_o_m_a_b.jpg'},
    {'name': 'faces/004_o_m_d_a.jpg', 'path': 'faces/004_o_m_d_a.jpg'},
    {'name': 'faces/004_o_m_d_b.jpg', 'path': 'faces/004_o_m_d_b.jpg'},
    {'name': 'faces/004_o_m_f_a.jpg', 'path': 'faces/004_o_m_f_a.jpg'},
    {'name': 'faces/004_o_m_f_b.jpg', 'path': 'faces/004_o_m_f_b.jpg'},
    {'name': 'faces/004_o_m_h_a.jpg', 'path': 'faces/004_o_m_h_a.jpg'},
    {'name': 'faces/004_o_m_h_b.jpg', 'path': 'faces/004_o_m_h_b.jpg'},
    {'name': 'faces/004_o_m_n_a.jpg', 'path': 'faces/004_o_m_n_a.jpg'},
    {'name': 'faces/004_o_m_n_b.jpg', 'path': 'faces/004_o_m_n_b.jpg'},
    {'name': 'faces/004_o_m_s_a.jpg', 'path': 'faces/004_o_m_s_a.jpg'},
    {'name': 'faces/004_o_m_s_b.jpg', 'path': 'faces/004_o_m_s_b.jpg'},
    {'name': 'faces/066_y_m_a_a.jpg', 'path': 'faces/066_y_m_a_a.jpg'},
    {'name': 'faces/066_y_m_a_b.jpg', 'path': 'faces/066_y_m_a_b.jpg'},
    {'name': 'faces/066_y_m_d_a.jpg', 'path': 'faces/066_y_m_d_a.jpg'},
    {'name': 'faces/066_y_m_d_b.jpg', 'path': 'faces/066_y_m_d_b.jpg'},
    {'name': 'faces/066_y_m_f_a.jpg', 'path': 'faces/066_y_m_f_a.jpg'},
    {'name': 'faces/066_y_m_f_b.jpg', 'path': 'faces/066_y_m_f_b.jpg'},
    {'name': 'faces/066_y_m_h_a.jpg', 'path': 'faces/066_y_m_h_a.jpg'},
    {'name': 'faces/066_y_m_h_b.jpg', 'path': 'faces/066_y_m_h_b.jpg'},
    {'name': 'faces/066_y_m_n_a.jpg', 'path': 'faces/066_y_m_n_a.jpg'},
    {'name': 'faces/066_y_m_n_b.jpg', 'path': 'faces/066_y_m_n_b.jpg'},
    {'name': 'faces/066_y_m_s_a.jpg', 'path': 'faces/066_y_m_s_a.jpg'},
    {'name': 'faces/066_y_m_s_b.jpg', 'path': 'faces/066_y_m_s_b.jpg'},
    {'name': 'faces/079_o_f_a_a.jpg', 'path': 'faces/079_o_f_a_a.jpg'},
    {'name': 'faces/079_o_f_a_b.jpg', 'path': 'faces/079_o_f_a_b.jpg'},
    {'name': 'faces/079_o_f_d_a.jpg', 'path': 'faces/079_o_f_d_a.jpg'},
    {'name': 'faces/079_o_f_d_b.jpg', 'path': 'faces/079_o_f_d_b.jpg'},
    {'name': 'faces/079_o_f_f_a.jpg', 'path': 'faces/079_o_f_f_a.jpg'},
    {'name': 'faces/079_o_f_f_b.jpg', 'path': 'faces/079_o_f_f_b.jpg'},
    {'name': 'faces/079_o_f_h_a.jpg', 'path': 'faces/079_o_f_h_a.jpg'},
    {'name': 'faces/079_o_f_h_b.jpg', 'path': 'faces/079_o_f_h_b.jpg'},
    {'name': 'faces/079_o_f_n_a.jpg', 'path': 'faces/079_o_f_n_a.jpg'},
    {'name': 'faces/079_o_f_n_b.jpg', 'path': 'faces/079_o_f_n_b.jpg'},
    {'name': 'faces/079_o_f_s_a.jpg', 'path': 'faces/079_o_f_s_a.jpg'},
    {'name': 'faces/079_o_f_s_b.jpg', 'path': 'faces/079_o_f_s_b.jpg'},
    {'name': 'faces/116_m_m_a_a.jpg', 'path': 'faces/116_m_m_a_a.jpg'},
    {'name': 'faces/116_m_m_a_b.jpg', 'path': 'faces/116_m_m_a_b.jpg'},
    {'name': 'faces/116_m_m_d_a.jpg', 'path': 'faces/116_m_m_d_a.jpg'},
    {'name': 'faces/116_m_m_d_b.jpg', 'path': 'faces/116_m_m_d_b.jpg'},
    {'name': 'faces/116_m_m_f_a.jpg', 'path': 'faces/116_m_m_f_a.jpg'},
    {'name': 'faces/116_m_m_f_b.jpg', 'path': 'faces/116_m_m_f_b.jpg'},
    {'name': 'faces/116_m_m_h_a.jpg', 'path': 'faces/116_m_m_h_a.jpg'},
    {'name': 'faces/116_m_m_h_b.jpg', 'path': 'faces/116_m_m_h_b.jpg'},
    {'name': 'faces/116_m_m_n_a.jpg', 'path': 'faces/116_m_m_n_a.jpg'},
    {'name': 'faces/116_m_m_n_b.jpg', 'path': 'faces/116_m_m_n_b.jpg'},
    {'name': 'faces/116_m_m_s_a.jpg', 'path': 'faces/116_m_m_s_a.jpg'},
    {'name': 'faces/116_m_m_s_b.jpg', 'path': 'faces/116_m_m_s_b.jpg'},
    {'name': 'faces/140_y_f_a_a.jpg', 'path': 'faces/140_y_f_a_a.jpg'},
    {'name': 'faces/140_y_f_a_b.jpg', 'path': 'faces/140_y_f_a_b.jpg'},
    {'name': 'faces/140_y_f_d_a.jpg', 'path': 'faces/140_y_f_d_a.jpg'},
    {'name': 'faces/140_y_f_d_b.jpg', 'path': 'faces/140_y_f_d_b.jpg'},
    {'name': 'faces/140_y_f_f_a.jpg', 'path': 'faces/140_y_f_f_a.jpg'},
    {'name': 'faces/140_y_f_f_b.jpg', 'path': 'faces/140_y_f_f_b.jpg'},
    {'name': 'faces/140_y_f_h_a.jpg', 'path': 'faces/140_y_f_h_a.jpg'},
    {'name': 'faces/140_y_f_h_b.jpg', 'path': 'faces/140_y_f_h_b.jpg'},
    {'name': 'faces/140_y_f_n_a.jpg', 'path': 'faces/140_y_f_n_a.jpg'},
    {'name': 'faces/140_y_f_n_b.jpg', 'path': 'faces/140_y_f_n_b.jpg'},
    {'name': 'faces/140_y_f_s_a.jpg', 'path': 'faces/140_y_f_s_a.jpg'},
    {'name': 'faces/140_y_f_s_b.jpg', 'path': 'faces/140_y_f_s_b.jpg'},
    {'name': 'faces/168_m_f_a_a.jpg', 'path': 'faces/168_m_f_a_a.jpg'},
    {'name': 'faces/168_m_f_a_b.jpg', 'path': 'faces/168_m_f_a_b.jpg'},
    {'name': 'faces/168_m_f_d_a.jpg', 'path': 'faces/168_m_f_d_a.jpg'},
    {'name': 'faces/168_m_f_d_b.jpg', 'path': 'faces/168_m_f_d_b.jpg'},
    {'name': 'faces/168_m_f_f_a.jpg', 'path': 'faces/168_m_f_f_a.jpg'},
    {'name': 'faces/168_m_f_f_b.jpg', 'path': 'faces/168_m_f_f_b.jpg'},
    {'name': 'faces/168_m_f_h_a.jpg', 'path': 'faces/168_m_f_h_a.jpg'},
    {'name': 'faces/168_m_f_h_b.jpg', 'path': 'faces/168_m_f_h_b.jpg'},
    {'name': 'faces/168_m_f_n_a.jpg', 'path': 'faces/168_m_f_n_a.jpg'},
    {'name': 'faces/168_m_f_n_b.jpg', 'path': 'faces/168_m_f_n_b.jpg'},
    {'name': 'faces/168_m_f_s_a.jpg', 'path': 'faces/168_m_f_s_a.jpg'},
    {'name': 'faces/168_m_f_s_b.jpg', 'path': 'faces/168_m_f_s_b.jpg'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2025.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var introductionClock;
var introduction_text;
var btn_start;
var trial_faceClock;
var image_stim;
var trial_responseClock;
var btn_anger_2;
var btn_disgust_2;
var btn_fear_2;
var btn_happiness_2;
var btn_neutrality_2;
var btn_sadness_2;
var end_screenClock;
var text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "introduction"
  introductionClock = new util.Clock();
  introduction_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'introduction_text',
    text: 'Welcome!\n\nIn this experiment, you will see a series of faces showing different emotional expressions.\n\nYour task is to identify which emotion is being expressed by selecting one of the buttons below each face.\n\nPlease try to respond as accurately and as quickly as possible.\n\nWhen you are ready to begin, press the Start button below.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  btn_start = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'btn_start',
    text: 'Start',
    font: 'Arvo',
    pos: [0, (- 0.3)],
    size: [0.35, 0.15],
    padding: null,
    anchor: 'center',
    ori: 0.0,
    units: psychoJS.window.units,
    color: 'white',
    fillColor: 'black',
    borderColor: 'black',
    colorSpace: 'rgb',
    borderWidth: 0.0,
    opacity: null,
    depth: -1,
    letterHeight: 0.04,
    bold: true,
    italic: false,
  });
  btn_start.clock = new util.Clock();
  
  // Initialize components for Routine "trial_face"
  trial_faceClock = new util.Clock();
  image_stim = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_stim', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0.15], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "trial_response"
  trial_responseClock = new util.Clock();
  btn_anger_2 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'btn_anger_2',
    text: 'Anger',
    font: 'Arvo',
    pos: [(- 0.4), (- 0.25)],
    size: [0.3, 0.12],
    padding: 0.02,
    anchor: 'center',
    ori: 0.0,
    units: psychoJS.window.units,
    color: 'white',
    fillColor: 'black',
    borderColor: 'black',
    colorSpace: 'rgb',
    borderWidth: 2.0,
    opacity: 1.0,
    depth: 0,
    letterHeight: 0.04,
    bold: true,
    italic: false,
  });
  btn_anger_2.clock = new util.Clock();
  
  btn_disgust_2 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'btn_disgust_2',
    text: 'Disgust',
    font: 'Arvo',
    pos: [0.0, (- 0.25)],
    size: [0.3, 0.12],
    padding: 0.02,
    anchor: 'center',
    ori: 0.0,
    units: psychoJS.window.units,
    color: 'white',
    fillColor: 'black',
    borderColor: 'black',
    colorSpace: 'rgb',
    borderWidth: 2.0,
    opacity: 1.0,
    depth: -1,
    letterHeight: 0.04,
    bold: true,
    italic: false,
  });
  btn_disgust_2.clock = new util.Clock();
  
  btn_fear_2 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'btn_fear_2',
    text: 'Fear',
    font: 'Arvo',
    pos: [0.4, (- 0.25)],
    size: [0.3, 0.12],
    padding: 0.02,
    anchor: 'center',
    ori: 0.0,
    units: psychoJS.window.units,
    color: 'white',
    fillColor: 'black',
    borderColor: 'black',
    colorSpace: 'rgb',
    borderWidth: 2.0,
    opacity: 1.0,
    depth: -2,
    letterHeight: 0.04,
    bold: true,
    italic: false,
  });
  btn_fear_2.clock = new util.Clock();
  
  btn_happiness_2 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'btn_happiness_2',
    text: 'Happiness',
    font: 'Arvo',
    pos: [(- 0.4), (- 0.4)],
    size: [0.3, 0.12],
    padding: 0.02,
    anchor: 'center',
    ori: 0.0,
    units: psychoJS.window.units,
    color: 'white',
    fillColor: 'black',
    borderColor: 'black',
    colorSpace: 'rgb',
    borderWidth: 2.0,
    opacity: 1.0,
    depth: -3,
    letterHeight: 0.04,
    bold: true,
    italic: false,
  });
  btn_happiness_2.clock = new util.Clock();
  
  btn_neutrality_2 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'btn_neutrality_2',
    text: 'Neutrality',
    font: 'Arvo',
    pos: [0.0, (- 0.4)],
    size: [0.3, 0.12],
    padding: 0.02,
    anchor: 'center',
    ori: 0.0,
    units: psychoJS.window.units,
    color: 'white',
    fillColor: 'black',
    borderColor: 'black',
    colorSpace: 'rgb',
    borderWidth: 2.0,
    opacity: 1.0,
    depth: -4,
    letterHeight: 0.04,
    bold: true,
    italic: false,
  });
  btn_neutrality_2.clock = new util.Clock();
  
  btn_sadness_2 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'btn_sadness_2',
    text: 'Sadness',
    font: 'Arvo',
    pos: [0.4, (- 0.4)],
    size: [0.3, 0.12],
    padding: 0.02,
    anchor: 'center',
    ori: 0.0,
    units: psychoJS.window.units,
    color: 'white',
    fillColor: 'black',
    borderColor: 'black',
    colorSpace: 'rgb',
    borderWidth: 2.0,
    opacity: 1.0,
    depth: -5,
    letterHeight: 0.04,
    bold: true,
    italic: false,
  });
  btn_sadness_2.clock = new util.Clock();
  
  // Initialize components for Routine "end_screen"
  end_screenClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Thank you for participating. \nYou may now close the browser window.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var introductionMaxDurationReached;
var introductionMaxDuration;
var introductionComponents;
function introductionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'introduction' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    introductionClock.reset();
    routineTimer.reset();
    introductionMaxDurationReached = false;
    // update component parameters for each repeat
    // reset btn_start to account for continued clicks & clear times on/off
    btn_start.reset()
    psychoJS.experiment.addData('introduction.started', globalClock.getTime());
    introductionMaxDuration = null
    // keep track of which components have finished
    introductionComponents = [];
    introductionComponents.push(introduction_text);
    introductionComponents.push(btn_start);
    
    for (const thisComponent of introductionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function introductionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'introduction' ---
    // get current time
    t = introductionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *introduction_text* updates
    if (t >= 0.0 && introduction_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      introduction_text.tStart = t;  // (not accounting for frame time here)
      introduction_text.frameNStart = frameN;  // exact frame index
      
      introduction_text.setAutoDraw(true);
    }
    
    
    // if introduction_text is active this frame...
    if (introduction_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *btn_start* updates
    if (t >= 0 && btn_start.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      btn_start.tStart = t;  // (not accounting for frame time here)
      btn_start.frameNStart = frameN;  // exact frame index
      
      btn_start.setAutoDraw(true);
    }
    
    
    // if btn_start is active this frame...
    if (btn_start.status === PsychoJS.Status.STARTED) {
    }
    
    if (btn_start.status === PsychoJS.Status.STARTED) {
      // check whether btn_start has been pressed
      if (btn_start.isClicked) {
        if (!btn_start.wasClicked) {
          // store time of first click
          btn_start.timesOn.push(btn_start.clock.getTime());
          // store time clicked until
          btn_start.timesOff.push(btn_start.clock.getTime());
        } else {
          // update time clicked until;
          btn_start.timesOff[btn_start.timesOff.length - 1] = btn_start.clock.getTime();
        }
        if (!btn_start.wasClicked) {
          // end routine when btn_start is clicked
          continueRoutine = false;
          
        }
        // if btn_start is still clicked next frame, it is not a new click
        btn_start.wasClicked = true;
      } else {
        // if btn_start is clicked next frame, it is a new click
        btn_start.wasClicked = false;
      }
    } else {
      // keep clock at 0 if btn_start hasn't started / has finished
      btn_start.clock.reset();
      // if btn_start is clicked next frame, it is a new click
      btn_start.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of introductionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function introductionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'introduction' ---
    for (const thisComponent of introductionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('introduction.stopped', globalClock.getTime());
    psychoJS.experiment.addData('btn_start.numClicks', btn_start.numClicks);
    psychoJS.experiment.addData('btn_start.timesOn', btn_start.timesOn);
    psychoJS.experiment.addData('btn_start.timesOff', btn_start.timesOff);
    // the Routine "introduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions_faces.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trial_faceRoutineBegin(snapshot));
      trialsLoopScheduler.add(trial_faceRoutineEachFrame());
      trialsLoopScheduler.add(trial_faceRoutineEnd(snapshot));
      trialsLoopScheduler.add(trial_responseRoutineBegin(snapshot));
      trialsLoopScheduler.add(trial_responseRoutineEachFrame());
      trialsLoopScheduler.add(trial_responseRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trial_faceMaxDurationReached;
var trial_faceMaxDuration;
var trial_faceComponents;
function trial_faceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_face' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    trial_faceClock.reset(routineTimer.getTime());
    routineTimer.add(0.250000);
    trial_faceMaxDurationReached = false;
    // update component parameters for each repeat
    image_stim.setImage(image_file);
    psychoJS.experiment.addData('trial_face.started', globalClock.getTime());
    trial_faceMaxDuration = null
    // keep track of which components have finished
    trial_faceComponents = [];
    trial_faceComponents.push(image_stim);
    
    for (const thisComponent of trial_faceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function trial_faceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_face' ---
    // get current time
    t = trial_faceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_stim* updates
    if (t >= 0 && image_stim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_stim.tStart = t;  // (not accounting for frame time here)
      image_stim.frameNStart = frameN;  // exact frame index
      
      image_stim.setAutoDraw(true);
    }
    
    
    // if image_stim is active this frame...
    if (image_stim.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_stim.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_stim.tStop = t;  // not accounting for scr refresh
      image_stim.frameNStop = frameN;  // exact frame index
      // update status
      image_stim.status = PsychoJS.Status.FINISHED;
      image_stim.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trial_faceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial_faceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_face' ---
    for (const thisComponent of trial_faceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trial_face.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (trial_faceMaxDurationReached) {
        trial_faceClock.add(trial_faceMaxDuration);
    } else {
        trial_faceClock.add(0.250000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trial_responseMaxDurationReached;
var clickedEmotion;
var trial_responseMaxDuration;
var trial_responseComponents;
function trial_responseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_response' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    trial_responseClock.reset();
    routineTimer.reset();
    trial_responseMaxDurationReached = false;
    // update component parameters for each repeat
    // reset btn_anger_2 to account for continued clicks & clear times on/off
    btn_anger_2.reset()
    // reset btn_disgust_2 to account for continued clicks & clear times on/off
    btn_disgust_2.reset()
    // reset btn_fear_2 to account for continued clicks & clear times on/off
    btn_fear_2.reset()
    // reset btn_happiness_2 to account for continued clicks & clear times on/off
    btn_happiness_2.reset()
    // reset btn_neutrality_2 to account for continued clicks & clear times on/off
    btn_neutrality_2.reset()
    // reset btn_sadness_2 to account for continued clicks & clear times on/off
    btn_sadness_2.reset()
    // Run 'Begin Routine' code from code_correctness_2
    clickedEmotion = "";
    
    psychoJS.experiment.addData('trial_response.started', globalClock.getTime());
    trial_responseMaxDuration = null
    // keep track of which components have finished
    trial_responseComponents = [];
    trial_responseComponents.push(btn_anger_2);
    trial_responseComponents.push(btn_disgust_2);
    trial_responseComponents.push(btn_fear_2);
    trial_responseComponents.push(btn_happiness_2);
    trial_responseComponents.push(btn_neutrality_2);
    trial_responseComponents.push(btn_sadness_2);
    
    for (const thisComponent of trial_responseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trial_responseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_response' ---
    // get current time
    t = trial_responseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *btn_anger_2* updates
    if (t >= 0 && btn_anger_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      btn_anger_2.tStart = t;  // (not accounting for frame time here)
      btn_anger_2.frameNStart = frameN;  // exact frame index
      
      btn_anger_2.setAutoDraw(true);
    }
    
    
    // if btn_anger_2 is active this frame...
    if (btn_anger_2.status === PsychoJS.Status.STARTED) {
    }
    
    if (btn_anger_2.status === PsychoJS.Status.STARTED) {
      // check whether btn_anger_2 has been pressed
      if (btn_anger_2.isClicked) {
        if (!btn_anger_2.wasClicked) {
          // store time of first click
          btn_anger_2.timesOn.push(btn_anger_2.clock.getTime());
          // store time clicked until
          btn_anger_2.timesOff.push(btn_anger_2.clock.getTime());
        } else {
          // update time clicked until;
          btn_anger_2.timesOff[btn_anger_2.timesOff.length - 1] = btn_anger_2.clock.getTime();
        }
        if (!btn_anger_2.wasClicked) {
          // end routine when btn_anger_2 is clicked
          continueRoutine = false;
          clickedEmotion = "anger";
        }
        // if btn_anger_2 is still clicked next frame, it is not a new click
        btn_anger_2.wasClicked = true;
      } else {
        // if btn_anger_2 is clicked next frame, it is a new click
        btn_anger_2.wasClicked = false;
      }
    } else {
      // keep clock at 0 if btn_anger_2 hasn't started / has finished
      btn_anger_2.clock.reset();
      // if btn_anger_2 is clicked next frame, it is a new click
      btn_anger_2.wasClicked = false;
    }
    
    // *btn_disgust_2* updates
    if (t >= 0 && btn_disgust_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      btn_disgust_2.tStart = t;  // (not accounting for frame time here)
      btn_disgust_2.frameNStart = frameN;  // exact frame index
      
      btn_disgust_2.setAutoDraw(true);
    }
    
    
    // if btn_disgust_2 is active this frame...
    if (btn_disgust_2.status === PsychoJS.Status.STARTED) {
    }
    
    if (btn_disgust_2.status === PsychoJS.Status.STARTED) {
      // check whether btn_disgust_2 has been pressed
      if (btn_disgust_2.isClicked) {
        if (!btn_disgust_2.wasClicked) {
          // store time of first click
          btn_disgust_2.timesOn.push(btn_disgust_2.clock.getTime());
          // store time clicked until
          btn_disgust_2.timesOff.push(btn_disgust_2.clock.getTime());
        } else {
          // update time clicked until;
          btn_disgust_2.timesOff[btn_disgust_2.timesOff.length - 1] = btn_disgust_2.clock.getTime();
        }
        if (!btn_disgust_2.wasClicked) {
          // end routine when btn_disgust_2 is clicked
          continueRoutine = false;
          clickedEmotion = "disgust";
        }
        // if btn_disgust_2 is still clicked next frame, it is not a new click
        btn_disgust_2.wasClicked = true;
      } else {
        // if btn_disgust_2 is clicked next frame, it is a new click
        btn_disgust_2.wasClicked = false;
      }
    } else {
      // keep clock at 0 if btn_disgust_2 hasn't started / has finished
      btn_disgust_2.clock.reset();
      // if btn_disgust_2 is clicked next frame, it is a new click
      btn_disgust_2.wasClicked = false;
    }
    
    // *btn_fear_2* updates
    if (t >= 0 && btn_fear_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      btn_fear_2.tStart = t;  // (not accounting for frame time here)
      btn_fear_2.frameNStart = frameN;  // exact frame index
      
      btn_fear_2.setAutoDraw(true);
    }
    
    
    // if btn_fear_2 is active this frame...
    if (btn_fear_2.status === PsychoJS.Status.STARTED) {
    }
    
    if (btn_fear_2.status === PsychoJS.Status.STARTED) {
      // check whether btn_fear_2 has been pressed
      if (btn_fear_2.isClicked) {
        if (!btn_fear_2.wasClicked) {
          // store time of first click
          btn_fear_2.timesOn.push(btn_fear_2.clock.getTime());
          // store time clicked until
          btn_fear_2.timesOff.push(btn_fear_2.clock.getTime());
        } else {
          // update time clicked until;
          btn_fear_2.timesOff[btn_fear_2.timesOff.length - 1] = btn_fear_2.clock.getTime();
        }
        if (!btn_fear_2.wasClicked) {
          // end routine when btn_fear_2 is clicked
          continueRoutine = false;
          clickedEmotion = "fear";
        }
        // if btn_fear_2 is still clicked next frame, it is not a new click
        btn_fear_2.wasClicked = true;
      } else {
        // if btn_fear_2 is clicked next frame, it is a new click
        btn_fear_2.wasClicked = false;
      }
    } else {
      // keep clock at 0 if btn_fear_2 hasn't started / has finished
      btn_fear_2.clock.reset();
      // if btn_fear_2 is clicked next frame, it is a new click
      btn_fear_2.wasClicked = false;
    }
    
    // *btn_happiness_2* updates
    if (t >= 0 && btn_happiness_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      btn_happiness_2.tStart = t;  // (not accounting for frame time here)
      btn_happiness_2.frameNStart = frameN;  // exact frame index
      
      btn_happiness_2.setAutoDraw(true);
    }
    
    
    // if btn_happiness_2 is active this frame...
    if (btn_happiness_2.status === PsychoJS.Status.STARTED) {
    }
    
    if (btn_happiness_2.status === PsychoJS.Status.STARTED) {
      // check whether btn_happiness_2 has been pressed
      if (btn_happiness_2.isClicked) {
        if (!btn_happiness_2.wasClicked) {
          // store time of first click
          btn_happiness_2.timesOn.push(btn_happiness_2.clock.getTime());
          // store time clicked until
          btn_happiness_2.timesOff.push(btn_happiness_2.clock.getTime());
        } else {
          // update time clicked until;
          btn_happiness_2.timesOff[btn_happiness_2.timesOff.length - 1] = btn_happiness_2.clock.getTime();
        }
        if (!btn_happiness_2.wasClicked) {
          // end routine when btn_happiness_2 is clicked
          continueRoutine = false;
          clickedEmotion = "happiness";
        }
        // if btn_happiness_2 is still clicked next frame, it is not a new click
        btn_happiness_2.wasClicked = true;
      } else {
        // if btn_happiness_2 is clicked next frame, it is a new click
        btn_happiness_2.wasClicked = false;
      }
    } else {
      // keep clock at 0 if btn_happiness_2 hasn't started / has finished
      btn_happiness_2.clock.reset();
      // if btn_happiness_2 is clicked next frame, it is a new click
      btn_happiness_2.wasClicked = false;
    }
    
    // *btn_neutrality_2* updates
    if (t >= 0 && btn_neutrality_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      btn_neutrality_2.tStart = t;  // (not accounting for frame time here)
      btn_neutrality_2.frameNStart = frameN;  // exact frame index
      
      btn_neutrality_2.setAutoDraw(true);
    }
    
    
    // if btn_neutrality_2 is active this frame...
    if (btn_neutrality_2.status === PsychoJS.Status.STARTED) {
    }
    
    if (btn_neutrality_2.status === PsychoJS.Status.STARTED) {
      // check whether btn_neutrality_2 has been pressed
      if (btn_neutrality_2.isClicked) {
        if (!btn_neutrality_2.wasClicked) {
          // store time of first click
          btn_neutrality_2.timesOn.push(btn_neutrality_2.clock.getTime());
          // store time clicked until
          btn_neutrality_2.timesOff.push(btn_neutrality_2.clock.getTime());
        } else {
          // update time clicked until;
          btn_neutrality_2.timesOff[btn_neutrality_2.timesOff.length - 1] = btn_neutrality_2.clock.getTime();
        }
        if (!btn_neutrality_2.wasClicked) {
          // end routine when btn_neutrality_2 is clicked
          continueRoutine = false;
          clickedEmotion = "neutrality";
        }
        // if btn_neutrality_2 is still clicked next frame, it is not a new click
        btn_neutrality_2.wasClicked = true;
      } else {
        // if btn_neutrality_2 is clicked next frame, it is a new click
        btn_neutrality_2.wasClicked = false;
      }
    } else {
      // keep clock at 0 if btn_neutrality_2 hasn't started / has finished
      btn_neutrality_2.clock.reset();
      // if btn_neutrality_2 is clicked next frame, it is a new click
      btn_neutrality_2.wasClicked = false;
    }
    
    // *btn_sadness_2* updates
    if (t >= 0 && btn_sadness_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      btn_sadness_2.tStart = t;  // (not accounting for frame time here)
      btn_sadness_2.frameNStart = frameN;  // exact frame index
      
      btn_sadness_2.setAutoDraw(true);
    }
    
    
    // if btn_sadness_2 is active this frame...
    if (btn_sadness_2.status === PsychoJS.Status.STARTED) {
    }
    
    if (btn_sadness_2.status === PsychoJS.Status.STARTED) {
      // check whether btn_sadness_2 has been pressed
      if (btn_sadness_2.isClicked) {
        if (!btn_sadness_2.wasClicked) {
          // store time of first click
          btn_sadness_2.timesOn.push(btn_sadness_2.clock.getTime());
          // store time clicked until
          btn_sadness_2.timesOff.push(btn_sadness_2.clock.getTime());
        } else {
          // update time clicked until;
          btn_sadness_2.timesOff[btn_sadness_2.timesOff.length - 1] = btn_sadness_2.clock.getTime();
        }
        if (!btn_sadness_2.wasClicked) {
          // end routine when btn_sadness_2 is clicked
          continueRoutine = false;
          clickedEmotion = "sadness";
        }
        // if btn_sadness_2 is still clicked next frame, it is not a new click
        btn_sadness_2.wasClicked = true;
      } else {
        // if btn_sadness_2 is clicked next frame, it is a new click
        btn_sadness_2.wasClicked = false;
      }
    } else {
      // keep clock at 0 if btn_sadness_2 hasn't started / has finished
      btn_sadness_2.clock.reset();
      // if btn_sadness_2 is clicked next frame, it is a new click
      btn_sadness_2.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trial_responseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var correct;
function trial_responseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_response' ---
    for (const thisComponent of trial_responseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trial_response.stopped', globalClock.getTime());
    psychoJS.experiment.addData('btn_anger_2.numClicks', btn_anger_2.numClicks);
    psychoJS.experiment.addData('btn_anger_2.timesOn', btn_anger_2.timesOn);
    psychoJS.experiment.addData('btn_anger_2.timesOff', btn_anger_2.timesOff);
    psychoJS.experiment.addData('btn_disgust_2.numClicks', btn_disgust_2.numClicks);
    psychoJS.experiment.addData('btn_disgust_2.timesOn', btn_disgust_2.timesOn);
    psychoJS.experiment.addData('btn_disgust_2.timesOff', btn_disgust_2.timesOff);
    psychoJS.experiment.addData('btn_fear_2.numClicks', btn_fear_2.numClicks);
    psychoJS.experiment.addData('btn_fear_2.timesOn', btn_fear_2.timesOn);
    psychoJS.experiment.addData('btn_fear_2.timesOff', btn_fear_2.timesOff);
    psychoJS.experiment.addData('btn_happiness_2.numClicks', btn_happiness_2.numClicks);
    psychoJS.experiment.addData('btn_happiness_2.timesOn', btn_happiness_2.timesOn);
    psychoJS.experiment.addData('btn_happiness_2.timesOff', btn_happiness_2.timesOff);
    psychoJS.experiment.addData('btn_neutrality_2.numClicks', btn_neutrality_2.numClicks);
    psychoJS.experiment.addData('btn_neutrality_2.timesOn', btn_neutrality_2.timesOn);
    psychoJS.experiment.addData('btn_neutrality_2.timesOff', btn_neutrality_2.timesOff);
    psychoJS.experiment.addData('btn_sadness_2.numClicks', btn_sadness_2.numClicks);
    psychoJS.experiment.addData('btn_sadness_2.timesOn', btn_sadness_2.timesOn);
    psychoJS.experiment.addData('btn_sadness_2.timesOff', btn_sadness_2.timesOff);
    // Run 'End Routine' code from code_correctness_2
    psychoJS.experiment.addData("clickedEmotion", clickedEmotion);
    correct = Number.parseInt((clickedEmotion === correct_emotion));
    psychoJS.experiment.addData("correct", correct);
    
    // the Routine "trial_response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var end_screenMaxDurationReached;
var end_screenMaxDuration;
var end_screenComponents;
function end_screenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end_screen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    end_screenClock.reset();
    routineTimer.reset();
    end_screenMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('end_screen.started', globalClock.getTime());
    end_screenMaxDuration = null
    // keep track of which components have finished
    end_screenComponents = [];
    end_screenComponents.push(text);
    
    for (const thisComponent of end_screenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function end_screenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_screen' ---
    // get current time
    t = end_screenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // if text is active this frame...
    if (text.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_screenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_screenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_screen' ---
    for (const thisComponent of end_screenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('end_screen.stopped', globalClock.getTime());
    // the Routine "end_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
