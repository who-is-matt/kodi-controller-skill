from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

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
        
    # The "handle_xxxx_intent" function is triggered by Mycroft when the
    # skill's intent is matched.  The intent is defined by the IntentBuilder()
    # pieces, and is triggered when the user's utterance matches the pattern
    # defined by the keywords.  In this case, the match occurs when one word
    # is found from each of the files:
    #    vocab/en-us/Hello.voc
    #    vocab/en-us/World.voc
    # In this example that means it would match on utterances like:
    #   'Hello world'
    #   'Howdy you great big world'
    #   'Greetings planet earth'
#    @intent_handler(IntentBuilder("").require("Hello").require("World"))
#    def handle_hello_world_intent(self, message):
        # In this case, respond by simply speaking a canned response.
        # Mycroft will randomly speak one of the lines from the file
        #    dialogs/en-us/hello.world.dialog
#        self.speak_dialog("hello.world")

#    @intent_handler(IntentBuilder("").require("Count").require("Dir"))
#    def handle_count_intent(self, message):
#        if message.data["Dir"] == "up":
#            self.count += 1
#        else:  # assume "down"
#            self.count -= 1
#        self.speak_dialog("count.is.now", data={"count": self.count})

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

    
    ### Connection controls
    @intent_handler(IntentBuilder("").require("KodiKeywords")).require("ConnectKeywords")
    def handle_direction_intent(self, message):
        self.speak_dialog("WIP")
    
    ### Playback controls
     @intent_handler(IntentBuilder("").require("KodiKeywords")).require("PlayPauseKeywords")
    def handle_direction_intent(self, message):
#        self.speak_dialog("WIP")
        myPlayerid = self.get_playerid()
        if myPlayerid != '':
            self.myKodi.Player.PlayPause(playerid=myPlayerid)
        else:
            self.speak_dialog("NotPlaying")
    @intent_handler(IntentBuilder("").require("KodiKeywords")).require("StopKeywords")
    def handle_direction_intent(self, message):
#        self.speak_dialog("WIP")
        myPlayerid = self.get_playerid()
        if myPlayerid != '':
            self.myKodi.Player.Stop(playerid=myPlayerid)
        else:
            self.speak_dialog("NotPlaying")    
    @intent_handler(IntentBuilder("").require("KodiKeywords")).require("SeekKeywords").require("ForwardKeywords")
    def handle_direction_intent(self, message):
#        self.speak_dialog("WIP")
        myPlayerid = self.get_playerid()
        if myPlayerid != '':
            self.myKodi.Player.Seek(playerid=myPlayerid, value="smallforward")
        else:
            self.speak_dialog("NotPlaying")    
    @intent_handler(IntentBuilder("").require("KodiKeywords")).require("SeekKeywords").require("BackKeywords")
    def handle_direction_intent(self, message):
#        self.speak_dialog("WIP")
        myPlayerid = self.get_playerid()
        if myPlayerid != '':
            self.myKodi.Player.Seek(playerid=myPlayerid, value="smallbackward")
        else:
            self.speak_dialog("NotPlaying")  
    
    ### Menu controls
    @intent_handler(IntentBuilder("").require("KodiKeywords")).require("DirectionKeywords")
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
            self.speak_dialog("WIP")
            # self.myKodi.Input.Right()     
     @intent_handler(IntentBuilder("").require("KodiKeywords")).require("InfoKeywords")
    def handle_direction_intent(self, message):
#        self.speak_dialog("WIP")
        self.myKodi.Input.Info()
     @intent_handler(IntentBuilder("").require("KodiKeywords")).require("OSDKeywords")
    def handle_direction_intent(self, message):
#        self.speak_dialog("WIP")
        self.myKodi.Input.ShowOSD()        
     @intent_handler(IntentBuilder("").require("KodiKeywords")).require("HomeKeywords")
    def handle_direction_intent(self, message):
#        self.speak_dialog("WIP")
        self.myKodi.Input.Home()        
     @intent_handler(IntentBuilder("").require("KodiKeywords")).require("BackKeywords")
    def handle_direction_intent(self, message):
#        self.speak_dialog("WIP")
        self.myKodi.Input.Back()        
     @intent_handler(IntentBuilder("").require("KodiKeywords")).require("ContextKeywords")
    def handle_direction_intent(self, message):
        self.myKodi.Input.ContextMenu()  
     @intent_handler(IntentBuilder("").require("KodiKeywords")).require("SelectKeywords")
    def handle_direction_intent(self, message):
#        self.speak_dialog("WIP")
        self.myKodi.Input.Select()          
        
    ### Libary controls
     @intent_handler(IntentBuilder("").require("KodiKeywords")).require("ScanKeywords").require("MovieKeywords")
    def handle_direction_intent(self, message):
#        self.speak_dialog("WIP")
        self.myKodi.VideoLibrary.Scan()      
    @intent_handler(IntentBuilder("").require("KodiKeywords")).require("ScanKeywords").require("MusicKeywords")
    def handle_direction_intent(self, message):
#        self.speak_dialog("WIP")
        self.myKodi.AudioLibrary.Scan()     
        
        
# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return KodiControllerSkill()
