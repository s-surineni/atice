public class Follower implements Observer {
    private String followerName;

    public Follower (String followerName) {
        this.followerName = followerName;
    }

    public void update (String status) {
        System.out.println("Updated status: " + status);
    }

    public void play() {
        System.out.println("Playing");
    }
}
