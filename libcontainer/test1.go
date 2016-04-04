package main

func main() {

	rootfs, err := newRootfs()
	ok(t, err)
	defer remove(rootfs)

	// Execute a long-running container
	container1, err := newContainer(newTemplateConfig(rootfs))
	ok(t, err)
	defer container1.Destroy()

	stdinR1, stdinW1, err := os.Pipe()
	ok(t, err)
	init1 := &libcontainer.Process{
		Cwd:   "/",
		Args:  []string{"cat"},
		Env:   standardEnvironment,
		Stdin: stdinR1,
	}
	err = container1.Start(init1)
	stdinR1.Close()
	defer stdinW1.Close()
	ok(t, err)

	// get the state of the first container
	state1, err := container1.State()
}
