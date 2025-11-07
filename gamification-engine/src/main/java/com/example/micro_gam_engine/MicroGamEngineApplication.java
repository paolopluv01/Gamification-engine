package com.example.micro_gam_engine;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MicroGamEngineApplication {

	public static void main(String[] args) {
		SpringApplication.run(MicroGamEngineApplication.class, args);
	}

}


/*
Quando invii questa richiesta, il flusso sarà completo:
1.  Il **Controller** riceve il JSON e lo mappa a `UserEventRequest`.
2.  Il **Controller** chiama `GamificationService.handleUserEvent()`.
3.  Il **Service** aggiorna lo stato e chiama `ChurnPredictionService.getChurnProbability()`.
4.  Il **Churn Service** effettua la chiamata HTTP all'ML Engine (Python FastAPI su `localhost:8000`).
5.  Il **Log** Java mostrerà la decisione strategica presa (se l'utente è ad alto rischio, stamperà
	l'allerta di retenzione).

Hai completato l'intera architettura dimostrativa, integrando ML (Python),
Analisi Dati e un back-end scalabile (Java/Spring Boot)!
*/