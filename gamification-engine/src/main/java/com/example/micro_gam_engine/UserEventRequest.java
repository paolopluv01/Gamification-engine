package com.example.micro_gam_engine;


/*Definiamo una semplice classe Java, UserEventRequest, per mappare i dati
che riceveremo tramite la richiesta HTTP (il payload JSON). */
/*Il client invia un corpo JSON a un endpoint POST, Spring ha pertanto bisogno di sapere
come convertire il JSON in un oggetto Java che possa manipolare.
Il meccanismo avviene grazie all'annotazione @RequestBody nel tuo controller:*/


public class UserEventRequest {
    private String userId;
    private String eventType;
    
    // Costruttore senza argomenti richiesto da Spring per la deserializzazione JSON
    public UserEventRequest() {}
    
    // Getter e Setter
    public String getUserId() {
        return userId;
    }
    public void setUserId(String userId) {
        this.userId = userId;
    }
    public String getEventType() {
        return eventType;
    }
    public void setEventType(String eventType) {
        this.eventType = eventType;
    }

}
    

