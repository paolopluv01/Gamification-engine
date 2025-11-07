package com.example.micro_gam_engine;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

@Configuration // 1. Indica che questa classe contiene definizioni di bean
public class AppConfig {

    /**
     * Definisce il bean RestTemplate per essere iniettato in altri servizi.
     * È necessario per le chiamate REST sincrone all'ML Engine.
     */
    @Bean // 2. Il metodo restituisce un oggetto gestito da Spring (un bean)
    public RestTemplate restTemplate() {
        // Qui potresti configurare timeout, intercettori, ecc.
        return new RestTemplate();
    }
}
/*
@Configuration: Quando Spring Boot si avvia, scansiona il package principale e trova questa classe.

@Bean: Spring esegue il metodo restTemplate() e prende l'istanza restituita (new RestTemplate()).

Registro nel Contenitore: Questa istanza di RestTemplate viene registrata nel Contenitore di Inversione di Controllo (IoC).

Risoluzione Dipendenza: Quando Spring incontra l'annotazione @Autowired nel tuo ChurnPredictionService
*/