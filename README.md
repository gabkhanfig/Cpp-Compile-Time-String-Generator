# Cpp-Compile-Time-String-Generator
Generates a c++ header file given the contents of chosen files with the file contents converted to constexpr const char*s

```
// Example of execution
python GenerateFile.py shaders Shaders.txt
```

The txt file used should have the absolute or relative paths to the files.

```
// Shaders.txt
C:/Users/SomePath/example.vert
C:/Users/SomePath/example.frag
```

The corresponding files can be any file.

```
// example.vert
#version 460 core
layout (location = 0) in vec3 aPos;
void main()
{
   gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
}

// example.frag
#version 460 core
out vec4 FragColor;
void main()
{
   FragColor = vec4(0.8f, 0.3f, 0.02f, 1.0f);
}
```

Resulting header file will look like this.

```
#pragma once

// Generated from example.vert
constexpr const char* generated_example_vert = R"(#version 460 core
layout (location = 0) in vec3 aPos;
void main()
{
   gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
})";

// Generated from example.frag
constexpr const char* generated_example_frag = R"(#version 460 core
out vec4 FragColor;
void main()
{
   FragColor = vec4(0.8f, 0.3f, 0.02f, 1.0f);
})";
```