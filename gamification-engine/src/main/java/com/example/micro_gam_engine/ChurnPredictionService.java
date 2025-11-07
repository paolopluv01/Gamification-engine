// ChurnPredictionService.java
package com.example.micro_gam_engine;

import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.client.RestTemplate;
import java.util.HashMap;
import java.util.Map;


@Service
public class ChurnPredictionService {

    // AGGIORNATO: Ora punta all'endpoint FastAPI
    private static final String ML_ENGINE_URL = "http://localhost:8000/predict_churn";
    
    @Autowired
    private RestTemplate restTemplate; // Richiede la configurazione di RestTemplate in AppConfig.java

    // Classe interna per mappare la risposta JSON dal servizio FastAPI
    public static class ChurnResponse {
        public double churn_probability;
        public String risk_level;
        // Getter e Setter omessi
    }

    /**
     * Chiama il microservizio ML e ottiene la probabilità di Churn.
     */
    public double getChurnProbability(User user) {
        // 1. Prepara il payload con le features che Spring invia a Python
        Map<String, Object> featuresPayload = new HashMap<>();
        featuresPayload.put("Recency", user.getDaysSinceLastLogin()); 
        featuresPayload.put("Frequency", user.getSumAllAccess()); // Assumi che User abbia un getter getFrequency()
        featuresPayload.put("Punti_Totali", user.getScore());
        featuresPayload.put("Engagement_Rate", user.getEngagementRate());
        featuresPayload.put("Volatilita_Punti_Std", user.getVolatilita_Punti_Std()); // Assumi che User abbia questo getter
        featuresPayload.put("Task_Completati", user.getTask_Completati());     // Assumi che User abbia questo getter

        try {
            // 2. Invia la richiesta POST al servizio FastAPI
            ChurnResponse response = restTemplate.postForObject(
                ML_ENGINE_URL, 
                featuresPayload, 
                ChurnResponse.class
            );
            
            return response != null ? response.churn_probability : 0.0;
        } catch (Exception e) {
            System.err.println("Errore nella chiamata all'ML Engine: " + e.getMessage());
            return 0.5; // Ritorna un valore di fallback in caso di errore
        }
    }
}