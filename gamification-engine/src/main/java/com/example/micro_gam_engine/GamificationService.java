package com.example.micro_gam_engine;

import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import java.util.HashMap;
import java.util.Map;
//import com.example.micro_gam_engine.ChurnPredictionService;
//import com.example.micro_gam_engine.User;
// GamificationService.java
@Service
public class GamificationService {

    @Autowired
    private ChurnPredictionService churnService;
    
    // (Simulazione DB - in realtà sarebbe un repository JPA)
    private Map<String, User> userDatabase = new HashMap<>();

    public String handleUserEvent(String userId, String eventType) {
    User user = userDatabase.getOrDefault(userId, new User(userId));
    String actionOutcome = "Nessuna azione strategica richiesta.";

        // 1. Logica di Assegnazione Punti e Aggiornamento Stato
    switch (eventType) {
        case "LOGIN":
            user.setScore(user.getScore() + 10); // Punti base
            user.setDaysSinceLastLogin(0); // Resetta la Recency!
            user.setSumAllAccess(user.getSumAllAccess() + 1);
            break;

        case "TASK_COMPLETED":
            user.setScore(user.getScore() + 150);
            user.setTask_Completati(user.getTask_Completati() + 1); // Aggiorna il contatore
            // Aggiorna Engagement Rate (ricorda che è un rapporto!)
            user.setEngagementRate(calculateNewEngagementRate(user, 1, 0)); 
            break;

        case "TASK_FAILED":
            user.setScore(user.getScore() + 0); // Nessun punto, magari una penalità minore
            // Aggiorna l'Engagement Rate in modo negativo
            user.setEngagementRate(calculateNewEngagementRate(user, 0, 1)); 
            break;

        case "RISCATTO_PREMIO":
            user.setScore(user.getScore() - 500); // Punti decurtati
            // Il riscatto è spesso un segnale positivo di loyalty, ma può anche precedere il churn.
            break;

        default:
            System.out.println("Evento non riconosciuto: " + eventType);
            actionOutcome = "Evento non gestito dal sistema.";
            break;
    }

        // --- 2. LOGICA ML (Interrogazione e Decisione) ---
    // ... (Il codice di ChurnPredictionService e la logica di restituzione rimangono invariati) ...
    double churnRisk = churnService.getChurnProbability(user);
    
    if (churnRisk >= 0.70) {
        System.out.println("ALERT! Utente " + userId + " a rischio ALTISSIMO...");
        actionOutcome = triggerRetentionChallenge(userId); 
    } else {
        System.out.println("Utente " + userId + " processato. Rischio: " + String.format("%.2f", churnRisk * 100) + "%. Nessuna azione strategica.");
        actionOutcome = "Nessuna azione strategica richiesta.";
    }

    userDatabase.put(userId, user); 
    return actionOutcome; 
}
    
    
    private String triggerRetentionChallenge(String userId) {
    // Invia una notifica o prepara la sfida
    String message = "Intervento: Inviata 'Sfida Esclusiva di Retenzione' per contrastare il rischio.";
    System.out.println("-> " + message);
    return message;
    }

    // Metodo di supporto per calcolare Engagement Rate (necessario nella classe)
private double calculateNewEngagementRate(User user, int completed, int failed) {
    int totalCompleted = user.getTask_Completati();
    int totalFailed = user.getTask_Falliti(); // Assumiamo un attributo e un getter per i task falliti
    
    int totalAttempts = totalCompleted + totalFailed + completed + failed;
    if (totalAttempts == 0) return 0.0;
    
    // Aggiorna anche TaskFalliti nell'oggetto User se è il caso
    if (failed > 0) user.setTask_Falliti(totalFailed + failed); 

    // Questa formula è semplificata, ma dimostra l'ingegneria feature-based
    return (double)(totalCompleted + completed) / totalAttempts;
}
}