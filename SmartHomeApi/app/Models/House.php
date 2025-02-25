<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Factories\HasFactory;


class House extends Model
{
    //
    use HasFactory;

    protected $fillable = [
        'houseName',
        'password',
        'apiKey',
        'clientKeyPath',
        'clientCertPath',
    ];
}
