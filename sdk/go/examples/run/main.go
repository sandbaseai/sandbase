// Command run calls any SandBase capability and prints the finished result.
//
//	go run ./examples/run exa/search '{"query":"AI agents","numResults":3}'
//	go run ./examples/run app-store/search '{"term":"notes"}'
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	sandbase "github.com/sandbaseai/sandbase/sdk/go"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintln(os.Stderr, "usage: run <model> ['<json params>']")
		os.Exit(1)
	}
	params := sandbase.Params{}
	if len(os.Args) > 2 {
		if err := json.Unmarshal([]byte(os.Args[2]), &params); err != nil {
			fmt.Fprintln(os.Stderr, "params must be a JSON object:", err)
			os.Exit(1)
		}
	}
	c, err := sandbase.NewClient("")
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	ctx, cancel := context.WithTimeout(context.Background(), 15*time.Minute)
	defer cancel()
	run, err := c.Run(ctx, os.Args[1], params)
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(2)
	}
	out, _ := json.MarshalIndent(run, "", "  ")
	fmt.Println(string(out))
}
