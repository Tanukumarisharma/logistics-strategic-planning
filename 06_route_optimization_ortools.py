from ortools.constraint_solver import pywrapcp, routing_enums_pb2

def solve_cvrp(dist_matrix, demands, vehicle_capacity, n_vehicles, depot=0):
    manager = pywrapcp.RoutingIndexManager(len(dist_matrix), n_vehicles, depot)
    routing = pywrapcp.RoutingModel(manager)

    def dist_cb(i, j):
        return int(dist_matrix[manager.IndexToNode(i)][manager.IndexToNode(j)])
    transit = routing.RegisterTransitCallback(dist_cb)
    routing.SetArcCostEvaluatorOfAllVehicles(transit)

    def demand_cb(i):
        return demands[manager.IndexToNode(i)]
    demand = routing.RegisterUnaryTransitCallback(demand_cb)
    routing.AddDimensionWithVehicleCapacity(
        demand, 0, [vehicle_capacity] * n_vehicles, True, "Capacity")

    params = pywrapcp.DefaultRoutingSearchParameters()
    params.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    params.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    params.time_limit.seconds = 30

    solution = routing.SolveWithParameters(params)
    routes = []
    for v in range(n_vehicles):
        idx, route = routing.Start(v), []
        while not routing.IsEnd(idx):
            route.append(manager.IndexToNode(idx))
            idx = solution.Value(routing.NextVar(idx))
        route.append(depot)
        routes.append(route)
    return routes, solution.ObjectiveValue()
