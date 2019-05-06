package in.makesimple.roadsense;

public class Pothole {
   private double Lat;
   private double Lon;

    public Pothole(double lat, double lon) {
        Lat = lat;
        Lon = lon;
    }

    public double getLat() {
        return Lat;
    }

    public double getLon() {
        return Lon;
    }
}
