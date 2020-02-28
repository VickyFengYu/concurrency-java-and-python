

import java.util.concurrent.Semaphore;

public class Building_H2O_1117 {
  Semaphore h, o;

  public Building_H2O_1117() {
    h = new Semaphore(2, true);
    o = new Semaphore(0, true);
  }

  public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
    h.acquire();
    releaseHydrogen.run();
    o.release();
  }

  public void oxygen(Runnable releaseOxygen) throws InterruptedException {
    o.acquire(2);
    releaseOxygen.run();
    h.release(2);
  }
}
