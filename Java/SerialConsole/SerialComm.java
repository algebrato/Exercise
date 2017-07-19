import gnu.io.*;
import java.awt.Color;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Enumeration;
import java.util.HashMap;
import java.util.TooManyListenersException;

public class SerialComm implements SerialPortEventListener{
	private Enumeration ports = null;
	private HashMap portMap = new HashMap();
	private CommPortIdentifier selectedPortIdentifier = null;
	private SerialPort serialPort = null;
	private InputStream input = null;
	private OutputStream output = null;
	private boolean bConnected = false;

	final static int TIMEOUT = 2000;

	final static int SPACE_ASCII = 32;
	final static int DASH_ASCII = 45;
	final static int NEW_LINE_ASCII = 10;

	String logText = "";

	public void searchForPorts(){
		ports = CommPortIdentifier.getPortIdentifiers();
		while (ports.hasMoreElements()){
			CommPortIdentifier curPort = (CommPortIdentifier)ports.nextElement();
			if (curPort.getPortType() == CommPortIdentifier.PORT_SERIAL){
				window.cboxPorts.addItem(curPort.getName());
				portMap.put(curPort.getName(), curPort);
			}
		}
	}

	public void connect(){
		String selectedPort = (String)window.cboxPorts.getSelectedItem();
		selectedPortIdentifier = (CommPortIdentifier)portMap.get(selectedPort);
		CommPort commPort = null;

		try{
			 commPort = selectedPortIdentifier.open("TigerControlPanel", TIMEOUT);
			 serialPort = (SerialPort)commPort;
			 setConnected(true);
			 logText = selectedPort + " opened successfully.";
			 window.txtLog.setForeground(Color.black);
			 window.txtLog.append(logText + "n");
			 window.keybindingController.toggleControls();
		}
		catch (PortInUseException e){
			logText = selectedPort + " is in use. (" + e.toString() + ")";
			window.txtLog.setForeground(Color.RED);
			window.txtLog.append(logText + "n");
		}
		catch (Exception e){
			logText = "Failed to open " + selectedPort + "(" + e.toString() + ")";
			window.txtLog.append(logText + "n");
			window.txtLog.setForeground(Color.RED);
		}
	}


}
