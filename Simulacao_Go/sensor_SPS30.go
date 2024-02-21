package main

import (
	"fmt"
	"math/rand"
	"time"
)

// simularLeituraSensor simula uma leitura do sensor SPS30, retornando dois valores, PM2.5 (µg/m³) e PM10 (µg/m³).
func simularLeituraSensor() (float64, float64) {
	var1 := rand.Float64() * 10
	var2 := rand.Float64()*10 + 10
	return var1, var2
}

func main() {
	// Simular leituras do sensor a cada segundo
	for i := 0; i < 10; i++ {
		var1, var2 := simularLeituraSensor()
		fmt.Printf("Leitura do sensor: %.2f, %.2f\n", var1, var2)
		time.Sleep(time.Second)
	}
}
