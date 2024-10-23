import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIClient {
    public static void main(String[] args) {
        try {
            // Locate the RMI registry
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            
            // Look up the remote object by name
            RemoteInterface remoteObject = (RemoteInterface) registry.lookup("Hello");
            
            // Call the remote method
            String response = remoteObject.sayHello("World");
            System.out.println(response);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
