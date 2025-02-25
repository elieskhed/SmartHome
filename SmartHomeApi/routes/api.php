<?php

use Illuminate\Support\Facades\Route;
use Illuminate\Http\Request;
use App\Http\Controllers\HouseController;
use App\Http\Controllers\InfluxDBController;



Route::prefix('house')->group(function(){
    Route::post('/create', [HouseController::class, 'create'])->name('house.create');
    Route::get('/data', [InfluxDBController::class, 'getAllData'])->name('house.data');
    // ex: http://172.20.10.5:8000/api/house/latestData?token=Wdp4HCPNvC3wHnvSfSwmVknhLuHtjUkoIzG6zPno
    Route::get('/latestData', [InfluxDBController::class, 'getLatestData'])->name('house.latestData');

    Route::get('/dataBySensor', [InfluxDBController::class, 'getDataBySensor'])->name('house.dataBySensor');
    Route::get('/dataAverage', [InfluxDBController::class, 'getAveragebySensor'])->name('house.averageData');
});