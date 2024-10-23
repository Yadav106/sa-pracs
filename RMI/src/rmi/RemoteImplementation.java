import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class RemoteImplementation extends UnicastRemoteObject implements RemoteInterface {
    public RemoteImplementation() throws RemoteException {
        super();
    }

    @Override
    public String sayHello(String name) throws RemoteException {
        return "Hello, " + name + "!";
    }
}
