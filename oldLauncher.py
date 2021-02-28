#! /usr/bin/python3.7
from common.logger import loggerDEBUG, loggerINFO, loggerWARNING, loggerERROR, loggerCRITICAL

def main():
    from dicts.ras_dic import PinsBuzzer, PinsDown, PinsOK
    from lib import Display, CardReader, PasBuz, Button
    from lib import OdooXMLrpc, Tasks, Utils

    Utils.migrationToVersion1_4_2()
    Utils.getSettingsFromDeviceCustomization()

    Buzz = PasBuz.PasBuz(PinsBuzzer)
    Disp = Display.Display()
    Reader = CardReader.CardReader()
    B_Down = Button.Button(PinsDown)
    B_OK = Button.Button(PinsOK)
    Hardware = [Buzz, Disp, Reader, B_Down, B_OK]

    Odoo = OdooXMLrpc.OdooXMLrpc(Disp)  
    Tasks = Tasks.Tasks(Odoo, Hardware)
    try:
        Disp.displayGreetings()

        Tasks.nextTask = "ensureOdoo" # TODO should be only ensure Odoo

        while True:
            if Tasks.nextTask:
                Disp.display_msg("connecting")
                Tasks.executeNextTask()
            else:
                Tasks.chooseTaskFromMenu()

    except Exception as e:
        loggerCRITICAL("Exception in main Loop of OLD Launcher", e)

if __name__ == "__main__":
    main()
