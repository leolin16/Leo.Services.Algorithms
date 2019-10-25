# CSharp

## History

### 1.0 - beginning

```C#
static void Main(string[] args)
{
    Console.WriteLine("Hello, World!");
}
```

### 2.0 - Generics Arrive, nullable value types and iteratives

```c#
static void Main(string[] args)
{
    List<string> names = new List<string>();
    names.Add("John");
    names.Add("Jane);

    int? age = null;

    foreach (string name in names)
    {
        Console.WriteLine("Name: {0}", name);
    }
}
```

### 3.0 - LINQ!, Lambda, Anonymous types

```c#
static void Main(string[] args)
{
    var widgets = from w in Widgets
                    where w.IsActive
                    select new
                    {
                        w.Name
                    };
    foreach (var widget in widgets)
    {
        Console.WriteLine("Name: {0}", widget.name);
    }
}
```

### 4.0 - Dynamic types

```c#
static void Main(string[] args)
{
    dynamic animal = new Dog();
    animal.ThisCompilesButIsNotGoingToWork();
}

### 5.0 - Async and Await

```c#
public async Task MarkWidgetAsInactive(int id)
{
    var target = await GetWidget(id);
    target.IsActive = false;
    await SaveChanges();
}
```

### 6.0 - Many Small Improvements - null propagating operator

```c#
public async Task<bool> IsWidgetActive(int id)
{
    var target = await GetWidget(id);
    // My favorite thing EVER
    return (target?.Isactive) ?? false;
}
```

### 7.0 - functional programming concepts - Expressions and Tuples (pattern matching)

```c#
static void main(string[] args)
{
    var pairs = new[]
    {
        (Left: Mark, Right: Mary),
        (Left: Jane, Right: John)
    };
    foreach (var pair in pairs)
    {
        Console.WriteLine($"Pair: {pair.Left} - {pair.Right}");
    }
}
```

### 8.0

1. Nullable Reference Types
2. Pattern Matching Improvements
3. Indices and Ranges
4. Default Interface Members(implementation inside)
5. Async Streams
6. Fast JSON Processing
7. Windows Desktop Support - creating WPF/WinForm applications on dotnet core 3.0