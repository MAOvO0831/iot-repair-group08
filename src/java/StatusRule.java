public class StatusRule {
    public enum Status { PENDING, PROCESSING, COMPLETED }

    public static boolean canTransition(Status current, Status target) {
        if (current == Status.PENDING && target == Status.PROCESSING) {
            return true;
        }
        if (current == Status.PROCESSING && target == Status.COMPLETED) {
            return true;
        }
        return false;
    }
}
