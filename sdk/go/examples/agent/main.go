// Command agent creates (or reuses) an Agent and runs one task in a Session.
//
//	go run ./examples/agent "What is 2+2?"                 # creates a small Agent
//	AGENT_ID=agt_... go run ./examples/agent "Summarize …"   # reuse a saved Agent
package main

import (
	"context"
	"fmt"
	"os"
	"time"

	sandbase "github.com/sandbaseai/sandbase/sdk/go"
)

func main() {
	input := "What is 2+2?"
	if len(os.Args) > 1 {
		input = os.Args[1]
	}
	c, err := sandbase.NewClient("")
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	ctx, cancel := context.WithTimeout(context.Background(), 15*time.Minute)
	defer cancel()

	agentID := os.Getenv("AGENT_ID")
	if agentID == "" {
		a, err := c.CreateAgent(ctx, sandbase.Params{
			"name": "Go example", "model": "deepseek/deepseek-v4-flash", "instructions": "Answer in one short sentence.",
		})
		if err != nil {
			fmt.Fprintln(os.Stderr, err)
			os.Exit(2)
		}
		agentID = a.ID
		fmt.Println("agent:", agentID)
	}
	res, err := c.RunAgent(ctx, agentID, input)
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(2)
	}
	fmt.Println("session:", res.SessionID)
	fmt.Println(res.Output)
}
