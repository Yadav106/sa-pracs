import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            // Create an instance of the remote object
            RemoteInterface remoteObject = new RemoteImplementation();
            
            // Create the RMI registry on port 1099
            Registry registry = LocateRegistry.createRegistry(1099);
            
            // Bind the remote object to the registry with a name
            registry.rebind("Hello", remoteObject);
            
            System.out.println("RMI Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
