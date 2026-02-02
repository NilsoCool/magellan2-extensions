package magellan.client.utils;

import java.io.File;

/**
 * A lightweight stub of the MagellanFinder class to allow ConsoleMerger to
 * compile
 * without depending on the full Magellan Client (Swing/Java9+) code.
 */
public class MagellanFinder {

    /**
     * Stub for finding the settings directory.
     * In a console context, we mimic the standard behavior.
     * 
     * @param resourceDir The base resource directory (can be null/ignored if we use
     *                    user home)
     * @param fileName    Optional filename to append
     * @return The directory or file for settings
     */
    public static File findSettingsDirectory(File resourceDir, String fileName) {
        // Standard Magellan behavior: check user home first
        File userHome = new File(System.getProperty("user.home"));
        File magellanDir = new File(userHome, ".magellan2");

        if (!magellanDir.exists()) {
            magellanDir.mkdirs();
        }

        if (fileName != null) {
            return new File(magellanDir, fileName);
        } else {
            return magellanDir;
        }
    }
}
