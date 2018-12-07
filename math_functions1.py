import math


posicion_x = 0.0
posicion_y = 0.0
velocidad = 0.0
e_velocidad = 0.0
pos_magnitud = 0.0
e_pos_magnitud = 0.0
e_aceleracion = 0.0
direccion = 0.0
e_posicion_x = 0.0
e_posicion_y = 0.0
error_estimado = 0.0
p_densidad = 0.0
p_hipotesis = 0.0
densidad_por_probabilidad = 0.0


def magnitude(x, y):
    return math.sqrt(math.pow(x, 2.0) + math.pow(y, 2.0))


def estimated_acceleration(prev_velocity, max_acceleration, d_velocity, acceleration_exponent=4):

    velocity_component = math.pow(float(prev_velocity)/float(d_velocity), acceleration_exponent)

    return max_acceleration * (1.0 - velocity_component)


def estimated_next_position(prev_pos_x, prev_pos_y, pos_x, pos_y, prev_velocity, e_acceleration, time_step):

    e_velocity = prev_velocity + time_step * e_acceleration

    direction = math.atan2(pos_y, pos_x)
    #direction = math.atan2(pos_y - prev_pos_y, pos_x - prev_pos_x)

    e_pos_x = pos_x + e_velocity * math.cos(direction) * time_step + \
              0.5 * e_acceleration * math.cos(direction) * math.pow(time_step, 2.0)

    e_pos_y = pos_y + e_velocity * math.sin(direction) * time_step + \
              0.5 * e_acceleration * math.sin(direction) * math.pow(time_step, 2.0)

    #para print
    global e_velocidad
    e_velocidad = e_velocity
    global direccion
    direccion = direction
    global e_posicion_x
    e_posicion_x = e_pos_x
    global e_posicion_y
    e_posicion_y = e_pos_y

    return e_pos_x, e_pos_y, e_velocity


def error(velocity, e_velocity, pos_x, pos_y, e_pos_x, e_pos_y):

    velocity_error = math.pow(velocity - e_velocity, 2.0)
    pos_magnitude = magnitude(pos_x, pos_y)
    e_pos_magnitude = magnitude(e_pos_x, e_pos_y)

    position_error = math.pow(pos_magnitude - e_pos_magnitude, 2.0)

    # para print
    global pos_magnitud
    pos_magnitud = pos_magnitude
    global e_pos_magnitud
    e_pos_magnitud = e_pos_magnitude

    return math.sqrt(velocity_error + position_error)


def probable_turn(prev_velocity, prev_pos_x, prev_pos_y, velocity, pos_x, pos_y, average):

    p_models = [0.18, 0.62, 0.2]
    p_acceleration_model = [[0.59, 0.25, 0.16], [0.25, 0.5, 0.25], [0.16, 0.4, 0.44]]
    # p_acceleration_model1 = [0.59, 0.25, 0.16]
    # p_acceleration_model2 = [0.25, 0.5, 0.25]
    # p_acceleration_model3 = [0.16, 0.4, 0.44]
    acceleration = [1.5, 2, 2.5]
    max_velocity = [13.33333, 15, 16.666667]
    time_step = 0.1
    total = 0.0
    e_next_position = ()
    probability_models = []

    for i, model in enumerate(p_models):
        #if i > 0:
        #    break
        for case in range(3):
            #if case > 0:
            #    break
            p_accel_model = p_acceleration_model[i][case]
            e_acceleration = estimated_acceleration(prev_velocity, acceleration[case], max_velocity[case])
            #print(e_acceleration)

            #para print


            e_next_position = estimated_next_position(pos_x, pos_y, prev_pos_x,
                                                      prev_pos_y, prev_velocity, e_acceleration, time_step)

            e_error = error(velocity, e_next_position[2], pos_x, pos_y,
                            e_next_position[0], e_next_position[1])
            p_density = (1.0 / (2.0 * math.pi * 1.2)) * math.exp(-1*(1.0/2.0) * math.pow(e_error, 2.0))
            p_hypothesis = 0.5 * model * p_accel_model
            total = total + p_hypothesis * p_density
            probability_models.append((p_hypothesis * p_density))

            # para print
            global posicion_x
            posicion_x = pos_x
            global posicion_y
            posicion_y = pos_y
            global velocidad
            velocidad = velocity
            global e_aceleracion
            e_aceleracion = e_acceleration
            global error_estimado
            error_estimado = e_error
            global p_densidad
            p_densidad = p_density
            global p_hipotesis
            p_hipotesis = p_hypothesis
            global densidad_por_probabilidad
            densidad_por_probabilidad = p_hypothesis * p_density

            # print("------------INICIO FILA---------------")
            # print("Posicion X  : " + str(posicion_x))
            # print("Posicion Y : " + str(posicion_y))
            # print("Velocidad : " + str(velocidad))
            # print("Aceleracion estimada : " + str(e_aceleracion))
            # print("Velocidad estimada : " + str(e_velocidad))
            # print("Magnitud Posicion : " + str(pos_magnitud))
            # print("Direccion : " + str(direccion))
            # print("Posicion X estimada : " + str(e_posicion_x))
            # print("Posicion Y estimada : " + str(e_posicion_y))
            # print("Magnitud Posicion estimada : " + str(e_pos_magnitud))
            # print("error : " + str(error_estimado))
            # print("Densidad de probabilidad : " + str(p_densidad))
            # print("Probabilidad H : " + str(p_hipotesis))
            # print("Densidad*Probabilidad H: " + str(densidad_por_probabilidad))
            # print(total)

    val_115 = probability_models[0] / total
    val_215 = probability_models[3] / total
    val_315 = probability_models[4] / total
    val_220 = probability_models[6] / total
    val_320 = probability_models[7] / total

    #print(val_115, val_215, val_315, val_220, val_320)


    p_turn = val_115 + val_215 + val_315 + val_220 + val_320
    #print(p_turn)


    #print(p_turn)
    #print(total)

    # print("------------INICIO FILA---------------")
    # print("Posicion X  : " + str(posicion_x))
    # print("Posicion Y : " + str(posicion_y))
    # print("Velocidad : " + str(velocidad))
    # print("Aceleracion estimada : " + str(e_aceleracion))
    # print("Velocidad estimada : " + str(e_velocidad))
    # print("Magnitud Posicion : " + str(pos_magnitud))
    # print("Direccion : " + str(direccion))
    # print("Posicion X estimada : " + str(e_posicion_x))
    # print("Posicion Y estimada : " + str(e_posicion_y))
    # print("Magnitud Posicion estimada : " + str(e_pos_magnitud))
    # print("error : " + str(error_estimado))
    # print("Densidad de probabilidad : " + str(p_densidad))
    # print("Probabilidad H : " + str(p_hipotesis))
    # print("Densidad*Probabilidad H: " + str(densidad_por_probabilidad))

    if p_turn > 0.6905 and average != 0:
        return 1, p_turn, e_next_position

    else:
        return 0, p_turn, e_next_position


