package com.example.micro_gam_engine;

// User.java (Modello Dati)
public class User {
    private String userId;
    private int score; // Punti Totali
    private int daysSinceLastLogin; // Corrisponde alla 'Recency'
    private double engagementRate; // Corrisponde alla 'Engagement_Rate'
    private int sumAllAccess; // Corrisponde alla 'Frequency'
    private double Volatilita_Punti_Std; // Corrisponde a 'Volatilita_Punti_Std'
    private int Task_Completati; // Corrisponde a 'TaskCompletati'
    private int Task_Falliti; // Corrisponde a 'TaskFalliti'

    public User(String userId) {
        this.userId = userId;
        this.score = 0;
        this.daysSinceLastLogin = 0;
        this.engagementRate = 0.0;
        this.sumAllAccess = 0;
        this.Volatilita_Punti_Std = 0.0;
        this.Task_Completati = 0;
        this.Task_Falliti = 0;
    }
    public String getUserId() {
        return userId;
    }
    public void setUserId(String userId) {
        this.userId = userId;
    }
    public int getScore() {
        return score;
    }
    public void setScore(int score) {
        this.score = score;
    }
    public int getDaysSinceLastLogin() {
        return daysSinceLastLogin;
    }
    public void setDaysSinceLastLogin(int daysSinceLastLogin) {
        this.daysSinceLastLogin = daysSinceLastLogin;
    }
    public double getEngagementRate() {
        return engagementRate;
    }
    public void setEngagementRate(double engagementRate) {
        this.engagementRate = engagementRate;
    }
    public int getSumAllAccess() {
        return sumAllAccess;
    }
    public void setSumAllAccess(int sumAllAccess) {
        this.sumAllAccess = sumAllAccess;
    }
    public double getVolatilita_Punti_Std() {
        return Volatilita_Punti_Std;
    }
    public int getTask_Completati() {
        return Task_Completati;
    }
    
    public void setTask_Completati(int Task_Completati) {
        this.Task_Completati = Task_Completati;
    }
    public int getTask_Falliti() {
        return Task_Falliti;
    }
    public void setTask_Falliti(int Task_Falliti) {
        this.Task_Falliti = Task_Falliti;
    }
    

}