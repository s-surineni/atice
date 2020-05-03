import java.util.List;
import java.util.ArrayList;


public class Channel implements Subject {
    private List<Observer> observerList;
    private String channelName;
    private String status;

    public Channel (String channelName, String status) {
        observerList = new ArrayList<Observer>();
        this.channelName = channelName;
        this.status = status;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
        notifyObservers();
    }

    public void notifyObservers () {
        for (Observer observer: observerList) {
            observer.update(status);
        }
    }

    public void registerObserver(Observer observer) {
        observerList.add(observer);
    }

    public void removeObserver(Observer observer) {
        observerList.remove(observer);
    }
}
