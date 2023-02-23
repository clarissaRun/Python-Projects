from os import system

#Alfabetos
def list_Alf(selec):
    alf_spanish="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    alf_english="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if selec==1:
        return alf_spanish
    elif selec==2:
        return alf_english
    else:
        return  0



def art_decor():
       system("cls")
       logo="""                                                      
          ::  ::   ::      ::::::::::   :::::::       ::    ::::::
        ::       ::  ::   ::           ::           ::   :: ::    :
       ::        ::  ::   ::             ::         ::   :: ::::::
       ::        ::__::   :::::::        ::::::::   ::___:: :::: 
       ::        ::  ::   ::                   ::   ::   :: ::  ::
        ::  ::   ::  ::   ::::::::::   ::::::::     ::   :: ::    ::
                                                                   
          ::  :: ::::::::  :::::::     ::      ::::::::   :::::: 
        ::          ::     ::    ::  ::   ::   ::         ::    : 
       ::           ::     ::    ::  ::   ::   ::         :::::: 
       ::           ::     :::::::   ::___::   :::::::    :::: 
       ::           ::     ::        ::   ::   ::         ::  :: 
        ::  ::   ::::::::  ::        ::   ::   :::::::::  ::   ::
        """
       print(logo)
         
    