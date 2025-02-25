<?php

namespace App\Http\Controllers;

use App\Models\House;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;
use Illuminate\Validation\ValidationException;
use Exception;

class HouseController extends Controller
{
    public function create(Request $request)
    {
        try {
            if (House::where('houseName', $request->input('houseName'))->exists()) {
                return response()->json([
                    'message' => "L'utilisateur est déjà existant."
                ], 409);
            }
            $validatedData = $request->validate([
                'houseName' => 'required|string|max:255|unique:houses,houseName',
                'password'  => [
                    'required',
                    'string',
                    'min:8',
                    'confirmed',
                    'regex:/[A-Z]/',
                    'regex:/[a-z]/',
                    'regex:/[0-9]/',
                    'regex:/[@$!%*?&]/'
                ],
            ], [
                'houseName.required' => 'Le nom de la maison est requis.',
                'houseName.string'   => 'Le nom de la maison doit être une chaîne de caractères.',
                'houseName.max'      => 'Le nom de la maison ne doit pas dépasser 255 caractères.',
                'houseName.unique'   => 'Ce nom de maison est déjà utilisé.',
                'password.required'  => 'Le mot de passe est requis.',
                'password.string'    => 'Le mot de passe doit être une chaîne de caractères.',
                'password.min'       => 'Le mot de passe doit contenir au moins 8 caractères.',
                'password.confirmed' => 'La confirmation du mot de passe ne correspond pas.',
                'password.regex'     => 'Le mot de passe doit contenir au moins une majuscule, une minuscule, un chiffre et un caractère spécial (@, $, !, %, *, ?, &).'
            ]);
            $houseName = $validatedData['houseName'];
            $plainPassword = $validatedData['password'];
            $hashedPassword = Hash::make($plainPassword); // (hashé en bcrypt)
            $apiKey = Str::random(40);
            $clientDir = '/etc/mosquitto/client';
            $caCertPath = '/etc/mosquitto/ca_certificates/CA.crt';
            $caKeyPath  = '/etc/mosquitto/ca_certificates/CA.key';
            if (!file_exists($clientDir)) {
                mkdir($clientDir, 0777, true);
            }
            $timestamp = time();
            $clientKeyPath  = "{$clientDir}/{$houseName}_{$timestamp}_client.key";
            $clientCsrPath  = "{$clientDir}/{$houseName}_{$timestamp}_client.csr";
            $clientCertPath = "{$clientDir}/{$houseName}_{$timestamp}_client.crt";
            $cmd = "openssl genrsa -out " . escapeshellarg($clientKeyPath) . " 2048";
            exec($cmd, $output, $return_var);
            if ($return_var !== 0) {
                throw new Exception("Erreur lors de la génération de la clé privée");
            }
            chmod($clientKeyPath, 0777);
            $subject = "/CN=" . $houseName;
            $cmd = "openssl req -new -key " . escapeshellarg($clientKeyPath)
                 . " -out " . escapeshellarg($clientCsrPath)
                 . " -subj " . escapeshellarg($subject);
            exec($cmd, $output, $return_var);
            if ($return_var !== 0) {
                throw new Exception("Erreur lors de la création de la demande de signature (CSR)");
            }
            chmod($clientCsrPath, 0777);
            $cmd = "openssl x509 -req -in " . escapeshellarg($clientCsrPath)
                 . " -CA " . escapeshellarg($caCertPath)
                 . " -CAkey " . escapeshellarg($caKeyPath)
                 . " -CAcreateserial -out " . escapeshellarg($clientCertPath)
                 . " -days 365 -sha256";
            exec($cmd, $output, $return_var);
            chmod($clientCertPath, 0777);
            if ($return_var !== 0) {
                $errorOutput = implode("\n", $output);
                throw new Exception("Erreur lors de la signature du certificat client. Détails: " . $errorOutput);
            }
            if (file_exists($clientCsrPath)) {
                unlink($clientCsrPath);
            }
            $clientKeyContents = file_get_contents($clientKeyPath);
            $clientCertContents = file_get_contents($clientCertPath);
            $caCertContents = file_get_contents($caCertPath);
            House::create([
                'houseName'      => $houseName,
                'password'       => $hashedPassword,
                'apiKey'         => $apiKey,
                'clientKeyPath'  => $clientKeyPath,
                'clientCertPath' => $clientCertPath,
            ]);
            return response()->json([
                'message'    => 'Maison créée avec succès.',
                'houseName'  => $houseName,
                'apiKey'     => $apiKey,
                'clientCert' => $clientCertContents,
                'caCert'     => $caCertContents,
                'clientKey'  => $clientKeyContents,
            ], 200);
        } catch (ValidationException $e) {
            return response()->json([
                'message' => 'Erreur de validation.',
                'errors'  => $e->errors(),
            ], 422);
        } catch (Exception $e) {
            return response()->json([
                'message' => 'Une erreur interne est survenue.',
                'error'   => $e->getMessage(),
            ], 500);
        }
    }
}
