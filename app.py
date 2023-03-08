#imports
import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False})

Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

#flask setup
app = Flask(__name__)

#flask routes - list all routes avaialable

@app.route("/"):
def honme():
    print("Server request for 'Home' page.")
    return ("Welcome to Surfs Up Weather API!<br><br>"
            f"Available Routes:<br>"
            f"/api/v1.0/precipitation<br>"
            f"/api/v1.0/stations<br>"
            f"/api/v1.0/tobs<br>"
            f"/api/v1.0/<start><br>"
            f"/api/v1.0/<start>/<end><br>"
    )


  # Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using `date` #as the key and `prcp` as the value.

    # Return the JSON representation of your dictionary.

    
    @app.route("/api/v1.0/precipitation")
    def precipitation():
        results = session.query(Measurent).all()
        session.close()
        
        year_prcp[]
        for result in results:
            year_prcp_dict = {}
            year_prcp_dict["date"] = result.date
            year_prcp_dict["prcp"] = result.prcp
            year_prcp.append(year_prcp_dict)
        return jsonify(year_prcp)
            
        
# * Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations"):
def stations():
    resullts = session.query(Station.station)all()
    session.close()
    all_station = list(np.ravel(results))
    return jsonify(all_station)

   
#Query the dates and temperature observations of the most-active station for the previous year of data.

    # Return a JSON list of temperature observations for the previous year.
    
@app.route("/api/v1.0/tobs"):
def temperatures():
    Last_Year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    temperature_results = session.query(Measurement.tob).filter(Measurement.date > Last_Year).all()
    session.close()
    
    temperature_list = list(np.ravel(temperature_results))
    return jsonify(temperature_list)

#Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end #range.

@app.route("/api/v1.0/<start>"):
def single_date(start):
    start_date = dt.datetime.strptime(start, &y-%m-%d)
  
    #For a specified start, calculate `TMIN`, `TAVG`, and `TMAX` for all the dates greater than or equal to the start date.
    summ_stats = session.query(func.min(Measurement.tob), fun.max(Measurement.tob), func.round(func.avg(Measurement.tob))).|
    filter(Measurement.date >= start_date).all()
    session.close()

   #For a specified start date and end date, calculate `TMIN`, `TAVG`, and `TMAX` for the dates from the start date to the end date, #inclusive.

@app.route("/api/v1.0/<start>/<end>"):
def trip_dates(start,end):
    Start_Date = dt.datetime.strptime(start,"%Y-%m-%d")
    End_Date = dt.datetime.strptime(end,"%Y-%m-%d")
    
    summary_stats = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.round(func.avg(Measurement.tobs))).\
    filter(Measurement.date.between(Start_Date,End_Date)).all()
    
    session.close()    
 
    summary = list(np.ravel(summary_stats))

# Jsonify summary
    return jsonify(summary)

if __name__ == "__main__":
     app.run(debug=True)
    