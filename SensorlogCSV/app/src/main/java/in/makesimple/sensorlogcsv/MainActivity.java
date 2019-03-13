package in.makesimple.sensorlogcsv;

import android.Manifest;
import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.format.DateFormat;
import android.util.Log;
import android.view.View;
import android.webkit.PermissionRequest;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.karumi.dexter.Dexter;
import com.karumi.dexter.MultiplePermissionsReport;
import com.karumi.dexter.PermissionToken;
import com.karumi.dexter.listener.multi.MultiplePermissionsListener;
import com.opencsv.CSVWriter;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

import static org.apache.commons.lang3.StringUtils.split;

public class MainActivity extends AppCompatActivity implements SensorEventListener , LocationListener {
    private SensorManager sensorManager;
    private Sensor gyroscopeSensor,accelerometerSensor;
    File file;
    CSVWriter writer;
    private TextView ax, ay, az,gx, gy, gz,speed;
    Boolean acc=false,gyr=false;
    String Ax=null,Ay=null,Az=null,Gx=null,Gy=null,Gz=null;
    Button buttonStart,buttonStop;
    LocationManager locationManager;
    Location newLocation;
    int v_speed;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Dexter.withActivity(this)
                .withPermissions(
                        android.Manifest.permission.ACCESS_FINE_LOCATION,
                        Manifest.permission.WRITE_EXTERNAL_STORAGE
                ).withListener(new MultiplePermissionsListener() {
            @Override
            public void onPermissionsChecked(MultiplePermissionsReport report) {/* ... */}

            @Override
            public void onPermissionRationaleShouldBeShown(List<com.karumi.dexter.listener.PermissionRequest> permissions, PermissionToken token) {

            }
        }).check();


        getLocation();

        ax = (TextView) findViewById(R.id.ax);
        ay = (TextView) findViewById(R.id.ay);
        az = (TextView) findViewById(R.id.az);
        gx = (TextView) findViewById(R.id.gx);
        gy = (TextView) findViewById(R.id.gy);
        gz = (TextView) findViewById(R.id.gz);
        buttonStart=(Button)findViewById(R.id.start);
        buttonStop=(Button)findViewById(R.id.stop);
        buttonStart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (accelerometerSensor == null) {
                    Toast.makeText(getApplicationContext(), "no accelerometer sensor", Toast.LENGTH_LONG).show();
                    return;
                }
                if (gyroscopeSensor==null){
                    Toast.makeText(getApplicationContext(),"No Gyro sensor",Toast.LENGTH_SHORT).show();
                    return;
                }

                String[] record = "TIME,Mills,Ax,Ay,Az,Gx,Gy,Gz,Lat,Lon,Speed".split(",");
                writer.writeNext(record);
                sensorManager.registerListener(MainActivity.this, sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER), 1);
                sensorManager.registerListener(MainActivity.this, sensorManager.getDefaultSensor(Sensor.TYPE_GYROSCOPE), 1);
            }
        });
        buttonStop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sensorManager.unregisterListener(MainActivity.this);
            }
        });
        String date = (DateFormat.format("dd-MM-yyyy hh:mm:ss", new java.util.Date()).toString());
        String csv = Environment.getExternalStorageDirectory()+"/"+ date+ ".csv";
        try {
            writer = new CSVWriter(new FileWriter(csv));
        } catch (IOException e) {
            e.printStackTrace();
        }
        sensorManager = (SensorManager) getSystemService(SENSOR_SERVICE);
        gyroscopeSensor = sensorManager.getDefaultSensor(Sensor.TYPE_GYROSCOPE);
        accelerometerSensor = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        gyroscopeSensor = sensorManager.getDefaultSensor(Sensor.TYPE_GYROSCOPE);


    }

    @Override
    public void onSensorChanged(SensorEvent event) {


        if(event.sensor.getType()==Sensor.TYPE_ACCELEROMETER &&!acc){
            Ax=String.format("%s", event.values[0]);
            Ay=String.format("%s", event.values[1]);
            Az=String.format("%s", event.values[2]);
            ax.setText(Ax);
            ay.setText(Ay);
            az.setText(Az);
            acc=true;

        }
        else if (event.sensor.getType()==Sensor.TYPE_GYROSCOPE && !gyr){
            Gx=String.format("%s", event.values[0]);
            Gy=String.format("%s", event.values[1]);
            Gz=String.format("%s", event.values[2]);
            gx.setText(Gx);
            gy.setText(Gy);
            gz.setText(Gz);
            gyr=true;
        }
        else if(acc && gyr){
            String time = (DateFormat.format("dd-MM-yyyy hh:mm:ss", new java.util.Date()).toString());
            long mill= System.currentTimeMillis();
            String[] record = (time+","+mill+","+Ax+","+Ay+","+Az+","+Gx+","+Gy+","+Gz+","+newLocation.getLatitude()+","+newLocation.getLongitude()+","+v_speed).split(",");
            writer.writeNext(record);
            acc=false;
            gyr=false;
        }


    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }

    @Override
    protected void onStop() {
        super.onStop();
        sensorManager.unregisterListener(MainActivity.this);
    }

    void getLocation() {
        try {
            locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, this);
        } catch (SecurityException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void onLocationChanged(Location location) {
        if (location != null) {
            newLocation = location;
            v_speed=(int) ((location.getSpeed()*3600)/1000);
        }
        Toast.makeText(getApplicationContext(), newLocation.getAccuracy() + "", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onStatusChanged(String provider, int status, Bundle extras) {

    }


    @Override
    public void onProviderEnabled(String provider) {

    }

    @Override
    public void onProviderDisabled(String provider) {
        Toast.makeText(MainActivity.this, "Please Enable GPS and Internet", Toast.LENGTH_SHORT).show();
    }
}
