#!/usr/bin/env python3

"""
This module is used to create calculations functions such as addition, subtraction, multiplication, and division.
This module will also be invoked as command line script using click.
"""

import click

def add(x, y):
    """
    This function adds two numbers.
    """
    return x + y

def subtract(x, y):
    """
    This function subtracts two numbers.
    """
    return x - y

def multiply(x, y):
    """
    This function multiplies two numbers.
    """
    return x * y

def divide(x, y):
    """
    This function divides two numbers.
    """
    return x / y


# build a click group
@click.group()
def cli():
    """
    This is the calculator app.
    """
    pass

# add subcommands to the click group
@cli.command("")
@click.argument('x', type=float)
@click.argument('y', type=float)
def add(x, y):
    """
    This function adds two numbers.
    """
    # invoke the add function with colored output using click
    click.echo(click.style(f"{x} + {y} = {x + y}", fg="green"))
@cli.command("subtract")

@click.argument('x', type=float)
@click.argument('y', type=float)
def subtract(x, y):
    """
    This function subtracts two numbers.
    """
    # invoke the subtract function with colored output using click
    click.echo(click.style(f"{x} - {y} = {x - y}", fg="red"))

@cli.command("product")
@click.argument('x', type=float)
@click.argument('y', type=float)
def multiply(x, y):
    """
    This function multiplies two numbers.
    """

    # invoke the multiply function with colored output using click
    click.echo(click.style(f"{x} * {y} = {x * y}", fg="blue"))
    
@cli.command("division")
@click.argument('x', type=float)
@click.argument('y', type=float)
def divide(x, y):
    """
    This function divides two numbers.
    """
    # invoke the divide function with colored output using click
    click.echo(click.style(f"{x} / {y} = {x / y}", fg="yellow"))
    

if __name__ == '__main__':
    cli()
