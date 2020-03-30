class CoffeeTouchscreenAdapter {
    private oldVendingMachine;

    public CoffeeTouchscreenAdapter(OldCoffeeMachine oldVendingMachine) {
        this.OldVendingMachine = oldVendingMachine;
    }

    public void chooseFirstSelection() {
        this.oldVendingMachine.selectA();
    }

    public void chooseSecondSelection() {
        this.oldVendingMachine.selectB();
    }
}
