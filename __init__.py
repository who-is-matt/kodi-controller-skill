from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from os import listdir, path
from os.path import dirname, join

from kodipydent import Kodi


class KodiControllerSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(KodiControllerSkill, self).__init__(name="KodiControllerSkill")
        
        # Initialize working variables used within the skill.
        
        self.myKodi = Kodi(self.settings["ip_address"], port=self.settings["port"], username=self.settings["user"], password=self.settings["password"])    
        
        self.vocabs = []
        
    def initialize(self):
        self._load_vocab_files() 
        self.settings.set_changed_callback(self.on_websettings_changed)
        self.on_websettings_changed()  
        
        ### Register intents
      
        # Connection controls
        connection_intent = IntentBuilder("ConnectionIntent").require("KodiKeywords").require("ConnectKeywords").build()
        self.register_intent(connection_intent, self.handle_connection_intent)        
        
        # Playback controls
        playpause_intent = IntentBuilder("PlayPauseIntent").require("KodiKeywords").require("PlayPauseKeywords").build()
        self.register_intent(playpause_intent, self.handle_playpause_intent) 

        stop_intent = IntentBuilder("StopIntent").require("KodiKeywords").require("StopKeywords").build()
        self.register_intent(stop_intent, self.handle_stop_intent) 

        seekforward_intent = IntentBuilder("SeekForwardIntent").require("KodiKeywords").require("SeekKeywords").require("ForwardKeywords").build()
        self.register_intent(seekforward_intent, self.handle_stop_intent)         

        seekback_intent = IntentBuilder("SeekBackIntent").require("KodiKeywords").require("SeekKeywords").require("BackKeywords").build()
        self.register_intent(seekback_intent, self.handle_seekback_intent)
        
        # Menu controls
        direction_intent = IntentBuilder("DirectionIntent").require("KodiKeywords").require("DirectionKeywords").build()
        self.register_intent(direction_intent, self.handle_direction_intent)
        
        info_intent = IntentBuilder("InfoIntent").require("KodiKeywords").require("InfoKeywords").build()
        self.register_intent(info_intent, self.handle_info_intent)
        
        osd_intent = IntentBuilder("InfoIntent").require("KodiKeywords").require("OSDKeywords").build()
        self.register_intent(osd_intent, self.handle_osd_intent)
        
        home_intent = IntentBuilder("InfoIntent").require("KodiKeywords").require("HomeKeywords").build()
        self.register_intent(home_intent, self.handle_home_intent)
        
        back_intent = IntentBuilder("InfoIntent").require("KodiKeywords").require("BackKeywords").build()
        self.register_intent(back_intent, self.handle_back_intent)
        
        context_intent = IntentBuilder("InfoIntent").require("KodiKeywords").require("ContextKeywords").build()
        self.register_intent(context_intent, self.handle_context_intent)
        
        select_intent = IntentBuilder("InfoIntent").require("KodiKeywords").require("SelectKeywords").build()
        self.register_intent(select_intent, self.handle_select_intent)
               
        # Library controls
        
        scanvideo_intent = IntentBuilder("InfoIntent").require("KodiKeywords")).require("ScanKeywords").require("MovieKeywords").build()
        self.register_intent(scanvideo_intent, self.handle_scanvideo_intent)
        
        scanaudio_intent = IntentBuilder("InfoIntent").require("KodiKeywords")).require("ScanKeywords").require("MovieKeywords").build()
        self.register_intent(scanaudio_intent, self.handle_scanaudio_intent)
        
    #################################################################         
    def _load_vocab_files(self):
        # Keep a list of all the vocabulary words for this skill.  Later
        # these words will be removed from utterances as part of the station
        # name.
        vocab_dir = join(dirname(__file__), 'vocab', self.lang)
        if path.exists(vocab_dir):
            for vocab_type in listdir(vocab_dir):
                if vocab_type.endswith(".voc"):
                    with open(join(vocab_dir, vocab_type), 'r') as voc_file:
                        for line in voc_file:
                            parts = line.strip().split("|")
                            vocab = parts[0]
                            self.vocabs.append(vocab)
        else:
            LOG.error('No vocab loaded, ' + vocab_dir + ' does not exist')    
            
    def on_websettings_changed(self):
        self.myKodi = Kodi(self.settings["ip_address"], port=self.settings["port"], username=self.settings["user"], password=self.settings["password"])

    def get_playerid(self):
        players = self.myKodi.Player.GetActivePlayers()['result']
        myPlayerid = ''
        for player in players:
            myPlayerid = player['playerid']   
        return myPlayerid
    
    #################################################################  
   
    ### Connection controls
    def handle_connection_intent(self):
        self.speak_dialog("WIP")
    
    ### Playback controls
    def handle_playpause_intent(self):
#        self.speak_dialog("WIP")
        myPlayerid = self.get_playerid()
        if myPlayerid != '':
            self.myKodi.Player.PlayPause(playerid=myPlayerid)
        else:
            self.speak_dialog("NotPlaying")

    def handle_stop_intent(self):
#        self.speak_dialog("WIP")
        myPlayerid = self.get_playerid()
        if myPlayerid != '':
            self.myKodi.Player.Stop(playerid=myPlayerid)
        else:
            self.speak_dialog("NotPlaying")    
            
    def handle_seekforward_intent(self):
#        self.speak_dialog("WIP")
        myPlayerid = self.get_playerid()
        if myPlayerid != '':
            self.myKodi.Player.Seek(playerid=myPlayerid, value="smallforward")
        else:
            self.speak_dialog("NotPlaying")       

    def handle_seekback_intent(self):
#        self.speak_dialog("WIP")
        myPlayerid = self.get_playerid()
        if myPlayerid != '':
            self.myKodi.Player.Seek(playerid=myPlayerid, value="smallbackward")
        else:
            self.speak_dialog("NotPlaying")  
   
    ### Menu controls
    def handle_direction_intent(self, message):
        if message.data["DirectionKeywords"] == "up": 
#            self.speak_dialog("WIP")
            self.myKodi.Input.Up()
        elif message.data["DirectionKeywords"] == "down":
#            self.speak_dialog("WIP")
            self.myKodi.Input.Down()
        elif message.data["DirectionKeywords"] == "left": 
#            self.speak_dialog("WIP")
            self.myKodi.Input.Left()
        else: 
#            self.speak_dialog("WIP")
            self.myKodi.Input.Right()     

    def handle_info_intent(self):
#        self.speak_dialog("WIP")
        self.myKodi.Input.Info()
    
    def handle_osd_intent(self):
#        self.speak_dialog("WIP")
        self.myKodi.Input.ShowOSD()      
    
    def handle_home_intent(self):
#        self.speak_dialog("WIP")
        self.myKodi.Input.Home()        
    
    def handle_back_intent(self):
#        self.speak_dialog("WIP")
        self.myKodi.Input.Back()  
    
    def handle_context_intent(self):
        self.myKodi.Input.ContextMenu()  
        
    def handle_select_intent(self):
#        self.speak_dialog("WIP")
        self.myKodi.Input.Select()          
        
    ### Libary controls

    def handle_scanvideo_intent(self):
##        self.speak_dialog("WIP")
        self.myKodi.VideoLibrary.Scan()  
    
    def handle_scanaudio_intent(self):
##        self.speak_dialog("WIP")
        self.myKodi.AudioLibrary.Scan()     
        
        
# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return KodiControllerSkill()
