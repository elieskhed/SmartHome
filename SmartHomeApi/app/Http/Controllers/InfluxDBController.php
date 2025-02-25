<?php

namespace App\Http\Controllers;
use Illuminate\Support\Facades\Http;


use Illuminate\Http\Request;

class InfluxDBController extends Controller
{
    //
    protected $influxHost = 'http://localhost:8086';
    protected $db         = 'intelighouse';


    public function getAllData(Request $request)
    {
        try {
            $token = $request->query('token');
            if (!$token) {
                return response()->json(['message' => 'Token non fourni'], 400);
            }
            $query = "SELECT * FROM mqtt_consumer WHERE house_token = '$token'";
            $response = Http::get($this->influxHost . '/query', [
                'db' => $this->db,
                'q'  => $query,
            ]);
            if ($response->failed()) {
                throw new Exception("Erreur lors de la récupération des données");
            }
            return response()->json(['data' => $response->json()], 200);
        } catch (Exception $e) {
            return response()->json([
                'message' => 'Erreur interne',
                'error'   => $e->getMessage()
            ], 500);
        }
    }

    public function getLatestData(Request $request){
        try {
            $token = $request->query('token');
            if (!$token) {
                return response()->json(['message' => 'Token non fourni'], 400);
            }
            $query = "SELECT * FROM mqtt_consumer WHERE house_token = '$token' ORDER BY time DESC LIMIT 1";
            $response = Http::get($this->influxHost . '/query', [
                'db' => $this->db,
                'q'  => $query,
            ]);
            if ($response->failed()) {
                throw new Exception("Erreur lors de la récupération des données");
            }
            return response()->json(['data' => $response->json()], 200);
        } catch (Exception $e) {
            return response()->json([
                'message' => 'Erreur interne',
                'error'   => $e->getMessage()
            ], 500);
        }
    }
    public function getDataBySensor(Request $request)
    {
        try {
            $token = $request->query('token');
            $sensorType = $request->query('sensorType');
            if (!$token || !$sensorType) {
                return response()->json([
                    'message' => 'Les paramètres token et sensorType sont requis'
                ], 400);
            }
            $query = "SELECT * FROM mqtt_consumer WHERE house_token = '$token' AND type = '$sensorType'";
            $response = Http::get($this->influxHost . '/query', [
                'db' => $this->db,
                'q'  => $query,
            ]);
            if ($response->failed()) {
                throw new Exception("Erreur lors de la récupération des données pour le capteur");
            }
            return response()->json(['data' => $response->json()], 200);
        } catch (Exception $e) {
            return response()->json([
                'message' => 'Erreur interne',
                'error'   => $e->getMessage()
            ], 500);
        }
    }

    public function getAverageDataBySensor(Request $request)
    {
        try {
            $token = $request->query('token');
            $sensorType = $request->query('sensorType');
            if (!$token || !$sensorType) {
                return response()->json([
                    'message' => 'Les paramètres token et sensorType sont requis'
                ], 400);
            }
            $query = "SELECT MEAN(value) FROM mqtt_consumer WHERE house_token = '$token' AND type = '$sensorType' GROUP BY time(1h) fill(null)";
            $response = Http::get($this->influxHost . '/query', [
                'db' => $this->db,
                'q'  => $query,
            ]);
            if ($response->failed()) {
                throw new Exception("Erreur lors de la récupération des données moyennes pour le capteur");
            }
            return response()->json(['data' => $response->json()], 200);
        } catch (Exception $e) {
            return response()->json([
                'message' => 'Erreur interne',
                'error'   => $e->getMessage()
            ], 500);
        }
    }
}
