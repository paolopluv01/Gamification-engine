package com.example.micro_gam_engine;

// GamificationController.java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController // Identifica questa classe come un gestore di richieste REST
@RequestMapping("/api/v1/gamification") // Definisce il percorso base per gli endpoint
public class GamificationController {

    @Autowired
    private GamificationService gamificationService;

    /**
     * Endpoint per ricevere un evento utente simulato.
     * Metodo: POST /api/v1/gamification/event
     */
    /*Nelle 2 righe sottostanti la classe UserEventRequest converte il json da client i un oggetto Java
     * tramite l'annotazione @RequestBody. Il metodo handleEvent non "usa" l'oggetto ResponseEntity<String>
     * nel senso di modificarlo, ma lo crea e lo restituisce.
     */
    @PostMapping("/event")
    public ResponseEntity<String> handleEvent(@RequestBody UserEventRequest request) {
        
        String userId = request.getUserId();
        String eventType = request.getEventType();
        
        if (userId == null || eventType == null || userId.isEmpty() || eventType.isEmpty()) {
            // Risposta 400 Bad Request se i dati sono mancanti
            return ResponseEntity.badRequest().body("Errore: userId e eventType sono campi obbligatori.");
        }

        try {
            // Chiama il servizio e cattura il risultato dell'azione
        String actionOutcome = gamificationService.handleUserEvent(userId, eventType);

        // Risposta 200 OK: include l'esito dell'azione
        return ResponseEntity.ok("Evento utente processato con successo. Esito azione: " + actionOutcome);

        } catch (Exception e) {
            // Risposta 500 Internal Server Error in caso di errore interno
            return ResponseEntity.internalServerError().body("Errore interno durante l'elaborazione dell'evento: " + e.getMessage());
        }
    }
}