package ptt.conan;
import java.io.*;
import java.net.*;

public class Conan{
  public static void main(String[] args) {
        String hostName="ptt.cc";
        int port=23;
        InetAddress address;

        /*if(args.length == 2) {
            hostName = args[0];
            port = Integer.parseInt(args[1]);
        }else{
          System.out.println("Usage: java JavaTelnet address port");
          return;
      }*/

        try {
            address = InetAddress.getByName(hostName);
            try {
                Socket socket = new Socket(address, port);
                new SocketToOut(socket).start();
                new InToSocket(socket).start();
            } catch (IOException e) {
              System.err.println("Connection failed");
            }
        }
        catch(UnknownHostException e) {
          System.err.println("Unknown host");
        }
    }
}

class SocketToOut extends Thread {
    private Socket socket;
  private BufferedReader socketIn;

    public SocketToOut(Socket socket) throws IOException{
        this.socket = socket;
      socketIn = new BufferedReader(new InputStreamReader(socket.getInputStream()));
    }

  @Override
    public void run() {
        try {
            String line = null;
            while((line = socketIn.readLine()) != null) {
            	System.out.println("123: "+line);
            }
            socket.close();
        } catch(IOException e) {
            System.out.println(e.toString());
        }
    }
}

class InToSocket extends Thread {
    private Socket socket;
  private PrintStream socketOut;
  private BufferedReader in;
  String comm;
    public InToSocket(Socket socket) throws IOException{
        this.socket = socket;
      socketOut = new PrintStream(socket.getOutputStream());
      in = new BufferedReader(new InputStreamReader(System.in));
    }

  @Override
    public void run(){
        try {
            while(!socket.isClosed()) {
            	comm=in.readLine();
            	socketOut.println(comm);
            	System.out.println(comm);
            }
        } catch(IOException e){
            e.printStackTrace();
        }
    }
}